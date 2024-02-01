import os
from pathlib import Path
import importlib
import requests
import subprocess
from tqdm import tqdm
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

def list_files_with_extensions(path: str, extensions: list, as_str=True, is_sorted=True, rel_path=False) -> list:
    paths = list()
    
    if isinstance(extensions, str):
        extensions = [extensions]
        
    files = [file for file in Path(path).rglob("*") if file.suffix in extensions]

    if rel_path:
        paths = [file.relative_to(path) for file in files]
    
    if is_sorted:
        paths = sorted(paths)
        
    if as_str:
        paths = [str(path) for path in paths]     
    
    return paths

def ckpt_downloader(model_name, model_type, model_url):
    root = folder_paths.folder_names_and_paths['models']
    local_path = r"%s\%s\%s" % (root, model_type, model_name)

    if os.path.exists(local_path):
        print(
            f"Model '{model_name}' already exists at '{local_path}'. Skipping download.")
        return

    if os.path.splitext(local_path)[1] == "":
        # git clone
        Path(local_path).parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(['git', 'clone', model_url, local_path])
    else:
        # download as file 
        Path(local_path).parent.mkdir(parents=True, exist_ok=True)
        response = requests.get(model_url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024  # 1 Kibibyte

        # 使用 tqdm 创建一个进度条
        progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)

        with open(local_path, 'wb') as file:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)

        progress_bar.close()
    print(
        f"Model '{model_name}' downloaded successfully to '{local_path}'")
    
    return True