#!/usr/bin/env python3

def file_extensions(filename):
    no_extension = []
    extensions = {}
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            index = line.rfind('.')
            if index == -1:
                no_extension.append(line)
            else:
                ext = line[index + 1:]
                if ext in extensions:
                    extensions[ext].append(line)
                else:
                    extensions[ext] = [line]
    return (no_extension, extensions)

def main():
    no_extension, extensions = file_extensions('src/filenames.txt')
    print(len(no_extension), 'files with no extension')
    for ext in sorted(extensions.keys()):
        print(ext, len(extensions[ext]))

if __name__ == "__main__":
    main()
