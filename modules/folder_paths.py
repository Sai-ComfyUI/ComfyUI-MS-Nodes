import os
from pathlib import Path

supported_pt_extensions = set(['.ckpt', '.pt', '.bin', '.pth', '.safetensors', 'onnx'])

root = Path(os.path.abspath(__file__))


folder_names_and_paths = {}

# install_check_file
folder_names_and_paths['version'] = r"%s\ms_1_0_0.ver" % root.parents[1]
folder_names_and_paths['requirement'] = r"%s\requirements.txt" % root.parents[1]

# folders level 1
folder_names_and_paths['assets'] = r"%s\assets" % root.parents[1]
folder_names_and_paths['py'] = r"%s\py" % root.parents[1]
folder_names_and_paths['models'] = r"%s\models" % root.parents[1]
folder_names_and_paths['modules'] = r"%s\modules" % root.parents[1]
folder_names_and_paths['packages'] = r"%s\packages" % root.parents[1]
# folders level 3
folder_names_and_paths['output'] = r"%s\output" % root.parents[3]


# packages
package_git_dict = {}
package_git_dict["Marigold"] = "https://github.com/prs-eth/Marigold"
package_git_dict["ms_MiDaS"] = "http://gitlab.moonshine.tw/ai/custom_packages/ms_MiDaS.git"
package_git_dict["ms_ZoeDepth"] = "http://gitlab.moonshine.tw/ai/custom_packages/ms_ZoeDepth.git"

# models
model_dict = {}
model_dict["Marigold"] = "https://huggingface.co/Bingxin/Marigold"
model_dict["ZoeD_M12_N"] = "https://github.com/isl-org/ZoeDepth/releases/download/v1.0/ZoeD_M12_N.pt"

