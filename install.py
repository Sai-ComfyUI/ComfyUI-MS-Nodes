import subprocess
import sys
import os

def pull_packages_by_dict(package_dict, package_root):
    for package in package_dict.keys():
        package_path = r"%s\%s" % (package_root, package)
        # print (package, package_dict[package], package_path)
        try:
            # Install the local package using the current Python interpreter
            if os.path.exists(package_path):
                subprocess.check_call(["git", "pull", package_dict[package],], cwd=package_path)
            else:
                subprocess.check_call(["git", "clone", package_dict[package], package_path])
                
            print(f"Successfully clone git from {package_dict[package]}")

        except subprocess.CalledProcessError as e:
            print(f"Error occurred while clone git from {package_dict[package]}: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")   


def install_local_package(package_dict, package_root):
    for package in package_dict.keys():
        package_path = r"%s\%s" % (package_root, package)
        
        try:
            # Ensure pip is available
            subprocess.check_call([sys.executable, "-m", "pip", "--version"])

            # Install the local package using the current Python interpreter
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_path])

            print(f"Successfully installed package from {package_path}")

        except subprocess.CalledProcessError as e:
            print(f"Error occurred while installing package from {package_path}: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    package_dict = {}
    package_dict["Marigold"] = "https://github.com/prs-eth/Marigold"
    package_dict["ms_MiDaS"] = "http://gitlab.moonshine.tw/ai/custom_packages/ms_MiDaS.git"
    package_dict["ms_ZoeDepth"] = "http://gitlab.moonshine.tw/ai/custom_packages/ms_ZoeDepth.git"
    
    pull_packages_by_dict(package_dict, r".\packages")
