import os

import first_script


if __name__ == "__main__":
    path = os.path.abspath("../application_programming_l1/dataset")
    path_to_files = first_script.get_path_to_files(path)
    first_script.write_as_csv(path, path_to_files)
