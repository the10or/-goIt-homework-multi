import shutil
import sys
from pathlib import Path
from normalize import normalize
from scan import scan, categories
from concurrent.futures import ThreadPoolExecutor


def main(path):
    scan(path)
    for category, files in categories.items():
        category_dir = path / category
        category_dir.mkdir(exist_ok=True)

        with ThreadPoolExecutor(10) as executor:
            executor.map(lambda file: move_files(category, file, path), files)

    scan(path)

    arch_path = Path(path / "archives")

    with ThreadPoolExecutor(10) as executor:
        executor.map(lambda arch: unpack_archives(arch, arch_path), arch_path.iterdir())


def unpack_archives(arch, arch_path):
    shutil.unpack_archive(arch, arch_path / arch.stem)
    arch.unlink()
    scan(arch_path)


def move_files(category, file, path):
    new_path = normalize(file.name)
    file.replace(path / category / new_path)


if __name__ == "__main__":
    main(Path(sys.argv[1]))
