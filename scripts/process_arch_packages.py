#!/usr/bin/env python3

input_file = r"..\arch_linux\arch_packages.md"
output_file = r"..\arch_linux\arch_packages.txt"

with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    for line in infile:
        stripped_line = line.strip()
        if not stripped_line or stripped_line.startswith("#"):
            continue
        if stripped_line.startswith("- "):
            stripped_line = stripped_line[2:]
        outfile.write(stripped_line + "\n")
