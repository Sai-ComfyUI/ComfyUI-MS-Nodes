import os
from pathlib import Path

def category_from_file(filepath):
    root = '%s/' % Path(__file__).parent.resolve()
    filepath = Path(filepath).parent
    relpath = (os.path.relpath(filepath, root))
    module_path = '/'.join(relpath.split('.')[0].split('\\'))
    category = "MS/%s" % (module_path)
    
    return category