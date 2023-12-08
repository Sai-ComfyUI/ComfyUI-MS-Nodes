import pathlib
import importlib
import os

root = pathlib.Path(__file__).parent.resolve()
nodes_folder = pathlib.Path('%s/nodes' % root)

py_files = list(nodes_folder.rglob("*.py"))

ui_files = [file for file in py_files if file.name.endswith(('_ui.py'))] 
ui_list = [file.name.split('.')[0] for file in ui_files]

NODE_CLASS_MAPPINGS = dict()
NODE_DISPLAY_NAME_MAPPINGS = dict()

for file in ui_files:
    relpath = (os.path.relpath(file, os.getcwd()))
    module_path = '.'.join(relpath.split('.')[0].split('\\'))
    ui_module = importlib.import_module(module_path)
    NODE_CLASS_MAPPINGS.update(ui_module.NODE_CLASS_MAPPINGS)
    NODE_DISPLAY_NAME_MAPPINGS.update(ui_module.NODE_DISPLAY_NAME_MAPPINGS)

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']XXX


