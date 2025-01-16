from typing import List
def get_names_from_file(filename: str = "names.txt") -> List:
    with open(filename, 'r') as file:
        content = [line.strip() for line in file.readlines()]
    return content

def get_unique_names(filename: str) -> List:
    names = get_names_from_file(filename)
    unique_names = list(set(names))
    return sorted(unique_names)