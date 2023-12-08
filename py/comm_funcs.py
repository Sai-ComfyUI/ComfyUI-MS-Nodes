import os
from pathlib import Path

def category_from_file(filepath):
    category = "MS/%s" % (Path(os.path.abspath(filepath)).parent).name
    return category