# ComfyUI-MS-Nodes

Custom nodes dev Document
===

## 目錄規範
* models / pt、onnx 等模型檔，根據用途分子資料夾
* modules / 通用的功能模組
* packages / 第三方或是自製分支版本
* py /  節點的 ui 跟 op 檔
* web /  js 等 custom widget 檔案 


## py / 節點 檔案命名
資料夾結構就是 comfyUI 裡的選單結構
* _ui: 節點界面  
只放界面定義跟一些簡單的計算，其他重要的計算都會放在 _op 裡
* _op: 同前綴 ui 檔會用到的方法  

## 其他

#### py\comm_func.py 通用的處理功能：

```
請注意這隻程式統一規範改放到主目錄下的 modules\comm_funcs.py,
如果有使用到這隻的請做改動，
檔案將在下一個 merge 版本正式移除(20231222 已移除)。
```

*  category_from_file(filepath, root_category = 'MS')->str 
根據檔案所在位置定義節點在選單的位置
*  import_path_to_module(filepath) 
將 .py 檔載入為 module
*  list_files_with_extensions(path: str, extensions: list, as_str=True, is_sorted=True) -> list 
列出目錄下（包括子目錄）指定副檔名的檔案清單，可以用來列出 model 或是其他檔案


#### modules\image_funcs.py 通用影像處理功能
用來放常用的影像處理(目前內容是直接複製 ken 寫的)
之後可以加入例如改變影像大小之類，運算中常用的簡單影像處理功能。

* pil_to_tensor pil 轉 tensor
* tensor_to_pil tensor 轉 pil
* tensor_to_cv2
* cv2_to_tensor
* cv2_to_pil


#### modules\folder_paths.py 靜態路徑變數
用來存放路徑變數，以 folder_paths.py 這個檔為中心點向外搜尋
folder_names_and_paths 字典用來放資料夾路徑，如果不存在會自動建立
checkfiles 用來放固定檔案，目前放 requirements.txt 和 .ver 版本檔（初次安裝以及更新會檢查）