# ComfyUI-MS-Nodes

Custom nodes dev Document

## 檔案命名  
* _ui: 節點界面  
只放界面定義跟一些簡單的計算，其他重要的計算都會放在 _op 裡
* _op: 同前綴 ui 檔會用到的方法  

## 其他

py\comm_func.py 這隻用來放通用的處理功能：

*  category_from_file(filepath, root_category = 'MS')->str 
根據檔案所在位置定義節點在選單的位置
*  import_path_to_module(filepath) 
將 .py 檔載入為 module
*  list_files_with_extensions(path: str, extensions: list, as_str=True, is_sorted=True) -> list 
列出目錄下（包括子目錄）指定副檔名的檔案清單，可以用來列出 model 或是其他檔案


