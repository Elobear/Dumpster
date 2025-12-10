import os
import sys

def print_tree(path, prefix=""):
    """Recursively prints a directory tree."""
    files = []
    dirs = []

    # Separate files and folders
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            dirs.append(entry)
        else:
            files.append(entry)

    # Print directories
    for i, d in enumerate(dirs):
        connector = "├── " if i < len(dirs) - 1 or files else "└── "
        print(prefix + connector + d)
        new_prefix = prefix + ("│   " if i < len(dirs) - 1 or files else "    ")
        print_tree(os.path.join(path, d), new_prefix)

    # Print files
    for i, f in enumerate(files):
        connector = "├── " if i < len(files) - 1 else "└── "
        print(prefix + connector + f)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python print_tree.py <path>")
        sys.exit(1)

    root_path = sys.argv[1]

    if not os.path.exists(root_path):
        print("Error: Path does not exist")
        sys.exit(1)

    print(os.path.basename(root_path) + "/")
    print_tree(root_path)
