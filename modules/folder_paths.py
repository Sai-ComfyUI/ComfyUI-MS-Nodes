import os
from pathlib import Path

supported_pt_extensions = set(['.ckpt', '.pt', '.bin', '.pth', '.safetensors', 'onnx'])

root = Path(os.path.abspath(__file__))

folder_names_and_paths = {}

folder_names_and_paths['assets'] = r"%s\assets" % root.parents[1]
folder_names_and_paths['py'] = r"%s\py" % root.parents[1]
folder_names_and_paths['models'] = r"%s\models" % root.parents[1]
folder_names_and_paths['modules'] = r"%s\modules" % root.parents[1]
folder_names_and_paths['packages'] = r"%s\packages" % root.parents[1]

folder_names_and_paths['output'] = r"%s\output" % root.parents[3]