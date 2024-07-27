import os
import argparse


def create_directory_structure(path, create_dirs):
    """
    Creates the specified directory structure for an ML/DL/LLM project.

    Args:
        path (str): The root path of the project.
        create_dirs (list): A list of directory paths to create.
    """
    for directory in create_dirs:
        full_path = os.path.join(path, directory)
        os.makedirs(full_path, exist_ok=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create project directory structure")
    parser.add_argument(
        "--path", type=str, default=".", help="Root path of the project"
    )
    parser.add_argument(
        "--create-dirs",
        type=str,
        nargs="+",
        default=["src", "notebooks", "app"],
        help="List of directories to create (e.g., --create-dirs src data models)",
    )

    args = parser.parse_args()

    create_directory_structure(args.path, args.create_dirs)
