import os


def get_next_exemplar(mark, id):
    return  os.path.abspath("..\\application_programming_l1\\dataset" + f"\\{mark}" + f"\\{id:04}.txt")