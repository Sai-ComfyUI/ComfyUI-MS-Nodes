import os
from pathlib import Path

def category_from_file(filepath, root_category = 'MS')->str:
    """_summary_

    Args:
        filepath (str): python file path
        root_category (str, optional): default category. Defaults to 'MS'.

    Returns:
        str: menu struct
    """
    root = '%s/' % Path(__file__).parent.resolve()
    filepath = Path(filepath).parent
    relpath = (os.path.relpath(filepath, root))
    module_path = '/'.join(relpath.split('.')[0].split('\\'))
    category = "%s/%s" % (root_category, module_path)
    
    return category