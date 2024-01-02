import subprocess
import sys
import os
from pathlib import Path
from .folder_paths import folder_names_and_paths, package_git_dict


def init_folders():
    for folder in folder_names_and_paths.keys():
        Path(folder_names_and_paths[folder]).mkdir(parents=True, exist_ok=True)


def install_packages_by_dict():
    package_git_dict
    package_root = folder_names_and_paths["packages"]

    for package in package_git_dict.keys():
        package_path = r"%s\%s" % (package_root, package)
        # print (package, package_git_dict[package], package_path)
        try:
            # Install the local package using the current Python interpreter
            if os.path.exists(package_path):
                subprocess.check_call(
                    ["git", "pull", package_git_dict[package],], cwd=package_path)
            else:
                subprocess.check_call(
                    ["git", "clone", package_git_dict[package], package_path])

            print(f"Successfully clone git from {package_git_dict[package]}")

        except subprocess.CalledProcessError as e:
            print(
                f"Error occurred while clone git from {package_git_dict[package]}: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


def run_setup():
    init_folders()
    install_packages_by_dict()
