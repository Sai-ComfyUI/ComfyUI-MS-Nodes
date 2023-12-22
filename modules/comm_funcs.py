import os
from pathlib import Path
import importlib
from importlib.machinery import SourceFileLoader
from . import folder_paths


def category_from_file(filepath, root_category='MS') -> str:
    """_summary_

    Args:
        filepath (str): python file path
        root_category (str, optional): default category. Defaults to 'MS'.

    Returns:
        str: menu struct
    """
    root = folder_paths.folder_names_and_paths['py']
    filepath = Path(filepath).parent
    relpath = (os.path.relpath(filepath, root))
    module_path = '/'.join(relpath.split('.')[0].split('\\'))
    category = "%s/%s" % (root_category, module_path)

    return category

def import_path_to_module(filepath):
    if Path(filepath).name.endswith('.py'):
        module_path = '.'.join(filepath.split('.')[0].split('\\'))
        module = importlib.import_module(module_path)
        return module  

def list_files_with_extensions(path: str, extensions: list, as_str=True, is_sorted=True) -> list:
    paths = list()
    
    if type(extensions) is str:
        extensions = [extensions]
        
    files = [file for file in Path(path).rglob("*") if file.suffix in extensions]
    
    if is_sorted:
        paths = sorted(files)
        
    if as_str:
        paths = [str(file) for file in files]
    
    return paths