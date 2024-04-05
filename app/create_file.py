import sys
import os
from datetime import datetime


def create_file(filename, content) -> None:
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(filename, 'w') as file:
        file.write(timestamp + '\n')

        for i, line in enumerate(content, start=1):
            file.write(f"{i} {line}\n")


def main() -> None:
    if len(sys.argv) < 3:
        return

    if '-d' in sys.argv and '-f' in sys.argv:
        directory_index = sys.argv.index('-d') + 1
        filename_index = sys.argv.index('-f') + 1

        directory_path = os.path.join(*sys.argv[directory_index:filename_index-1])
        filename = sys.argv[filename_index]
        os.makedirs(directory_path, exist_ok=True)

        content = []
        while True:
            line = input("Enter content line: ")
            if line.lower() == 'stop':
                break
            content.append(line.strip())
        file_path = os.path.join(directory_path, filename)
        create_file(file_path, content)

    elif '-f' in sys.argv:
        filename_index = sys.argv.index('-f') + 1
        filename = sys.argv[filename_index]

        content = []
        while True:
            line = input("Enter content line: ")
            if line.lower() == 'stop':
                break
            content.append(line.strip())

        create_file(filename, content)


if __name__ == "__main__":
    main()
