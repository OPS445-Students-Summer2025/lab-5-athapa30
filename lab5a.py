#!/usr/bin/env python3
# Author ID: athapa30

def read_file_string(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except Exception as e:
        return "error: could not read file"

def read_file_list(filename):
    try:
        with open(filename, "r") as f:
            return [line.strip() for line in f]  # Strip newlines
    except Exception as e:
        return ["error: could not read file"]

if __name__ == '__main__':
    with open("data.txt", "w") as f:
        f.write("Hello World\n")
        f.write("This is the second line\n")
        f.write("Third line\n")
        f.write("Last line\n")
