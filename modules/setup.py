import subprocess
import sys
import os
from pathlib import Path
from .folder_paths import folder_names_and_paths, package_git_dict, checkfiles


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

def install_requirement():
    requirement_file = checkfiles['requirement']
    version_file = checkfiles["version"]
    if not os.path.isfile(version_file):
        for file_path in Path(version_file).parent.iterdir():
            if file_path == ".ver":
                file_path.unlink()
                print("Old version detected")
                
        subprocess.check_call(["python", "-m", "pip", "install", "-r", requirement_file])
        with Path(version_file).open(mode='w') as file:
            file.write("This is a sample file.")

    print("Successfully update requirement")

def run_setup():
    init_folders()
    install_packages_by_dict()
    install_requirement()
