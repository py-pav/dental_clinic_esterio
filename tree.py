import os
import sys


def generate_tree(directory, prefix="", ignore_dirs=[".git", "__pycache__", ".idea"]):
    """Генерирует древовидную структуру директории"""
    if not os.path.isdir(directory):
        return f"{directory} не является директорией"

    items = []
    try:
        items = sorted(os.listdir(directory))
    except PermissionError:
        return f"{prefix}└── [Permission Denied]"

    tree_str = ""
    pointers = ["├── "] * (len(items) - 1) + ["└── "]

    for pointer, item in zip(pointers, items):
        path = os.path.join(directory, item)

        # Пропускаем игнорируемые директории
        if item in ignore_dirs or item.startswith('.'):
            continue

        tree_str += prefix + pointer + item + "\n"

        if os.path.isdir(path):
            extension = "│   " if pointer == "├── " else "    "
            tree_str += generate_tree(path, prefix + extension, ignore_dirs)

    return tree_str


if __name__ == "__main__":
    start_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    print(generate_tree(start_dir))