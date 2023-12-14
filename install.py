import subprocess
import sys
import os

# local_packages = ["./modules/modules_name"]
# remote_git_url = ["https://github.com/xinntao/facexlib",]

local_packages = []
remote_git_url = []

def git_pull_package(git_url):
    package_name = git_url.split("/")[-1]
    package_path = r"modules\%s" % package_name
    
    try:
        # Install the local package using the current Python interpreter
        if os.path.exists(package_path):
            subprocess.check_call(["git", "pull", git_url,], cwd=package_path)
        else:
            subprocess.check_call(["git", "clone", git_url, package_path])
            
        print(f"Successfully clone git from {git_url}")

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while clone git from {git_url}: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")    


def install_local_package(path_to_package):
    """
    Installs a local Python package using the Python interpreter executing this script.

    Args:
    - path_to_package (str): Relative or absolute path to the package directory containing setup.py.
    """
    try:
        # Ensure pip is available
        subprocess.check_call([sys.executable, "-m", "pip", "--version"])

        # Install the local package using the current Python interpreter
        subprocess.check_call([sys.executable, "-m", "pip", "install", path_to_package])

        print(f"Successfully installed package from {path_to_package}")

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing package from {path_to_package}: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    # Specify the path to your local package
    for git_url in remote_git_url:
        git_pull_package(git_url)
    for path_to_package in local_packages:
        # Check if the path exists
        if os.path.exists(path_to_package):
            install_local_package(path_to_package)
        else:
            print(f"Path {path_to_package} does not exist. Please check and try again.")

