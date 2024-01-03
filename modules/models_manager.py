import os
import requests
from tqdm import tqdm
from pathlib import Path
import subprocess
from .folder_paths import folder_names_and_paths


class MS_CKPT:
    def __init__(self, model_name, model_type, model_url, local_path):
        self.model_name = model_name
        self.model_type = model_type
        self.model_url = model_url
        self.local_path = local_path

    def download_model(self):
        # 检测本地路径是否已经有模型文件存在
        if os.path.exists(self.local_path):
            print(
                f"Model '{self.model_name}' already exists at '{self.local_path}'. Skipping download.")
            return
        
        Path(self.local_path).parent.mkdir(parents=True, exist_ok=True)
        
        if os.path.splitext(self.local_path)[1] == "":
            # git clone
            Path(self.local_path).parent.mkdir(parents=True, exist_ok=True)
            subprocess.run(['git', 'clone', self.model_url, self.local_path])
            print(f"Repository '{self.model_name}' downloaded successfully to '{self.local_path}'")
        else:
            response = requests.get(self.model_url, stream=True)
            total_size = int(response.headers.get('content-length', 0))
            block_size = 1024  # 1 Kibibyte

            # 使用 tqdm 创建一个进度条
            progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)

            with open(self.local_path, 'wb') as file:
                for data in response.iter_content(block_size):
                    progress_bar.update(len(data))
                    file.write(data)

            progress_bar.close()

        print(
            f"Model '{self.model_name}' downloaded successfully to '{self.local_path}'")
        
        return True

    def change_model_name(self, new_name):
        _, extension = os.path.splitext(self.local_path)
        new_path = os.path.join(os.path.dirname(
            self.local_path), f"{new_name}{extension}")
        os.rename(self.local_path, new_path)
        self.model_name = new_name
        self.local_path = new_path
        print(
            f"Model name changed to '{new_name}', file renamed to '{new_path}'")


model_folder = folder_names_and_paths['models']

# depth models 
depth_model_list =[
    MS_CKPT(model_name='dpt_beit_large_512',
                             model_type='depth',
                             model_url='https://github.com/isl-org/MiDaS/releases/download/v3_1/dpt_beit_large_512.pt',
                             local_path=(r'%s\Depth\dpt_beit_large_512.pt' % model_folder)
                             ),
    MS_CKPT(model_name='dpt_beit_large_384',
                             model_type='depth',
                             model_url='https://github.com/isl-org/MiDaS/releases/download/v3_1/dpt_beit_large_384.pt',
                             local_path=(r'%s\Depth\dpt_beit_large_384.pt' % model_folder)
                             ),
    MS_CKPT(model_name='dpt_beit_base_384',
                             model_type='depth',
                             model_url='https://github.com/isl-org/MiDaS/releases/download/v3_1/dpt_beit_base_384.pt',
                             local_path=(r'%s\Depth\dpt_beit_base_384.pt' % model_folder)
                             ),
    MS_CKPT(model_name='dpt_swin2_large_384',
                             model_type='depth',
                             model_url='https://github.com/isl-org/MiDaS/releases/download/v3_1/dpt_swin2_large_384.pt',
                             local_path=(r'%s\Depth\dpt_swin2_large_384.pt' % model_folder)
                             ),
    MS_CKPT(model_name='dpt_swin2_base_384',
                             model_type='depth',
                             model_url='https://github.com/isl-org/MiDaS/releases/download/v3_1/dpt_swin2_base_384.pt',
                             local_path=(r'%s\Depth\dpt_swin2_base_384.pt' % model_folder)
                             ),
    MS_CKPT(model_name='dpt_swin2_tiny_256',
                             model_type='depth',
                             model_url='https://github.com/isl-org/MiDaS/releases/download/v3_1/dpt_swin2_tiny_256.pt',
                             local_path=(r'%s\Depth\dpt_swin2_tiny_256.pt' % model_folder)
                             ),
    MS_CKPT(model_name='dpt_swin_large_384',
                             model_type='depth',
                             model_url='https://github.com/isl-org/MiDaS/releases/download/v3_1/dpt_swin_large_384.pt',
                             local_path=(r'%s\Depth\dpt_swin_large_384.pt' % model_folder)
                             ),
    MS_CKPT(model_name='dpt_next_vit_large_384',
                             model_type='depth',
                             model_url='https://github.com/isl-org/MiDaS/releases/download/v3_1/dpt_next_vit_large_384.pt',
                             local_path=(r'%s\Depth\dpt_next_vit_large_384.pt' % model_folder)
                             ),
    MS_CKPT(model_name='dpt_levit_224',
                             model_type='depth',
                             model_url='https://github.com/isl-org/MiDaS/releases/download/v3_1/dpt_levit_224.pt',
                             local_path=(r'%s\Depth\dpt_levit_224.pt' % model_folder)
                             ),
    MS_CKPT(model_name='dpt_large_384',
                             model_type='depth',
                             model_url='https://github.com/isl-org/MiDaS/releases/download/v3/dpt_large_384.pt',
                             local_path=(r'%s\Depth\dpt_large_384.pt' % model_folder)
                             ),
    MS_CKPT(model_name='dpt_hybrid_384',
                             model_type='depth',
                             model_url='https://github.com/isl-org/MiDaS/releases/download/v3/dpt_hybrid_384.pt',
                             local_path=(r'%s\Depth\dpt_hybrid_384.pt' % model_folder)
                             ),
    MS_CKPT(model_name='midas_v21_384',
                             model_type='depth',
                             model_url='https://github.com/isl-org/MiDaS/releases/download/v2_1/midas_v21_384.pt',
                             local_path=(r'%s\Depth\midas_v21_384.pt' % model_folder)
                             ),
    MS_CKPT(model_name='midas_v21_small_256',
                             model_type='depth',
                             model_url='https://github.com/isl-org/MiDaS/releases/download/v2_1/midas_v21_small_256.pt',
                             local_path=(r'%s\Depth\midas_v21_small_256.pt' % model_folder)
                             ),
    MS_CKPT(model_name='Marigold',
                             model_type='depth',
                             model_url='https://huggingface.co/Bingxin/Marigold',
                             local_path=(r'%s\Depth\Marigold' % model_folder)
                             ),
    
    
    ]
