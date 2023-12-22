from pathlib import Path
# import importlib
# from importlib.machinery import SourceFileLoader
import os, sys
from .modules import comm_funcs

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

WEB_DIRECTORY = "./web"
MODEL_DIRECTORY = "./models"

root = Path(__file__).parent.resolve()
py_folder = Path('%s/py' % root)
custom_nodes_path = Path(root).parents[1]

py_files = list(py_folder.rglob("*.py"))

ui_files = [file for file in py_files if file.name.endswith(('_ui.py'))] 
ui_list = [file.name.split('.')[0] for file in ui_files]

NODE_CLASS_MAPPINGS = dict()
NODE_DISPLAY_NAME_MAPPINGS = dict()

for file in ui_files:
    relpath = (os.path.relpath(file, custom_nodes_path))
    ui_module = comm_funcs.import_path_to_module(relpath)
    NODE_CLASS_MAPPINGS.update(ui_module.NODE_CLASS_MAPPINGS)
    NODE_DISPLAY_NAME_MAPPINGS.update(ui_module.NODE_DISPLAY_NAME_MAPPINGS)


__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']


