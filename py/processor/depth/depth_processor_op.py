import os
import torch
import numpy as np
from PIL import Image
from ....modules import folder_paths
from ....modules import image_funcs
from ....modules import models_manager
from ....packages.ms_ZoeDepth.zoedepth.utils.misc import save_raw_16bit, colorize
from ....packages.ms_MiDaS.run_ms import midas_color_to_depth
from ....packages.Marigold.marigold import MarigoldPipeline
import matplotlib
from matplotlib.colors import Normalize
from pathlib import Path


depth_models_folder = r"%s\Depth" % folder_paths.folder_names_and_paths['models']
packages_folder = folder_paths.folder_names_and_paths['packages']
ms_ZoeDepth_path = r"%s\ms_ZoeDepth" % packages_folder
ms_MiDaS = r"%s\ms_MiDaS" % packages_folder

depth_model_list = models_manager.depth_model_list

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

depth_models = dict()
depth_models['ZoeD_M12_N'] = None
depth_models['dpt_hybrid-midas'] = None
depth_models['dpt_large-midas'] = None
depth_models['midas_v21'] = None


def image_to_depth_with_model(depth_model, image):
    if depth_model == 'ZoeD_M12_N':
        colored_depth, colored_depth = resolve_zoe_depth(depth_model, image)
    else:
        colored_depth, colored_depth = resolve_midas_depth(depth_model, image)
    return (colored_depth, colored_depth)


def resolve_zoe_depth(depth_model, image):
    if depth_models['ZoeD_M12_N'] == None:
        model_path = r"%s\%s.pt" % (depth_models_folder, depth_model)
        if not os.path.isfile(model_path):
            Path(depth_models_folder).mkdir(parents=True, exist_ok=True)
            torch.hub.download_url_to_file("https://github.com/isl-org/ZoeDepth/releases/download/v1.0/ZoeD_M12_N.pt", model_path)
        depth_models['ZoeD_M12_N'] = torch.hub.load(ms_ZoeDepth_path, "ZoeD_N", source="local", path=model_path, pretrained=True).to(DEVICE)
        # depth_models['ZoeD_M12_N'] = torch.hub.load(ms_ZoeDepth_path, "ZoeD_N", source="local", pretrained=True).to(DEVICE)
    image = image_funcs.tensor_to_pil(image)
    depth_zoe_n = depth_models['ZoeD_M12_N'].infer_pil(image)
    colored = colorize(depth_zoe_n)
    colored_depth = image_funcs.pil_to_tensor(colored)
    return (colored_depth, colored_depth)


def resolve_midas_depth(depth_model, image):
    input_path = (r"%s\input.png" % ms_MiDaS)
    model_path=(r"%s\%s.pt" % (depth_models_folder, depth_model))
    [model.download_model() for model in depth_model_list if model.model_name == depth_model]
    image = image_funcs.tensor_to_pil(image)
    w, h = image.size
    image.save(input_path)
    output_path = midas_color_to_depth(input_path=input_path,
                                       output_path=(r"%s\output.png" % ms_MiDaS),
                                       model_path=model_path,
                                       model_type=os.path.splitext(depth_model)[0],
                                       optimize=False,
                                       side=False,
                                       height=h,
                                       square=False,
                                       grayscale=False)
    image = Image.open(output_path)
    grayscale_depth = image.convert("L").convert("RGB")
    grayscale_depth = image_funcs.pil_to_tensor(grayscale_depth)
    colored_depth = image_funcs.pil_to_tensor(image)
    return (colored_depth, grayscale_depth)


def resolve_marigold_depth(image, ensemble_size, denoising_steps, half_precision, processing_res, output_processing_res, seed, batch_size, color_map, apple_silicon):
    [model.clone_repo() for model in depth_model_list if model.model_name == "Marigold"]
    image = image_funcs.tensor_to_pil(image)
    if apple_silicon:
        if torch.backends.mps.is_available() and torch.backends.mps.is_built():
            DEVICE = torch.device("mps:0")
        else:
            DEVICE = torch.device("cpu")
    else:
        if torch.cuda.is_available():
            DEVICE = torch.device("cuda")
        else:
            DEVICE = torch.device("cpu")

    dtype = torch.float32
    if half_precision:
        dtype = torch.float16

    torch.manual_seed(seed)

    checkpoint_path = "%s\Marigold" % depth_models_folder
    pipe = MarigoldPipeline.from_pretrained(checkpoint_path, torch_dtype=dtype)

    try:
        import xformers
        pipe.enable_xformers_memory_efficient_attention()
    except Exception as e:
        print(e)
        pass  # run without xformers

    pipe = pipe.to(DEVICE)
    with torch.no_grad():
        input_image = image
        # Predict depth
        pipe_out = pipe(
            input_image,
            denoising_steps=denoising_steps,
            ensemble_size=ensemble_size,
            processing_res=processing_res,
            match_input_res=output_processing_res,
            batch_size=batch_size,
            color_map=color_map,
            show_progress_bar=True,
        )

        depth_pred: np.ndarray = pipe_out.depth_np
        depth_colored: Image.Image = pipe_out.depth_colored
        # exr_depth = (depth_pred * 65535.0).astype(np.uint16)
        # exr_depth_file = r"%s\exr_depth.png" % folder_paths.folder_names_and_paths['output']
        # Image.fromarray(exr_depth).save(exr_depth_file, mode="I;16")
        depth_grayscale = (depth_pred*255).astype(np.uint8)
        depth_grayscale = Image.fromarray(depth_grayscale).convert('RGB')

        colored_depth = image_funcs.pil_to_tensor(depth_colored)
        grayscale_depth = image_funcs.pil_to_tensor(depth_grayscale)
        
    return (colored_depth, grayscale_depth)


def colorize_depth(tensor_image, colorize_method, depth_min, depth_max, depth_mid_point):
    # print (tensor_image.min(), tensor_image.max())
    # normalized_tensor = (tensor_image - tensor_image.min()) / (tensor_image.max() - tensor_image.min())
    # tensor_image = (normalized_tensor * 255).to(torch.float32)
    # print (tensor_image.dtype)
    
    pil_image = image_funcs.tensor_to_pil(tensor_image)
    gray_image = pil_image.convert('L')
    gray_array = np.array(gray_image)
    normalized_gray = gray_array / 255.0
    
    colormap = matplotlib.colormaps[colorize_method]
    norm = Normalize(vmin=0, vmax=1, clip=False)
    norm.autoscale(normalized_gray)
    norm.vmin = depth_min
    norm.vmax = depth_max
    midpoint = depth_mid_point
    adjusted_gray = norm(normalized_gray - midpoint) + 0.5
    adjusted_gray = np.clip(adjusted_gray, 0, 1)
    color_image = (colormap(adjusted_gray) * 255).astype(np.uint8)
    pil_image = Image.fromarray(color_image.squeeze()).convert("RGBA")

    tensor_image = image_funcs.pil_to_tensor(pil_image)

    return (tensor_image)