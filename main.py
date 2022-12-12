import os

import first_script
import second_script
import third_script
import fourth_script


if __name__ == "__main__":
    path = os.path.abspath("../application_programming_l1/dataset")
    path_to_files = first_script.get_path_to_files(path)
    first_script.write_as_csv(path, path_to_files)
    new_dataset_path = second_script.copy_dataset(path)
    second_script.write_as_csv(new_dataset_path, path_to_files)
    third_script.create_copy(path)
    copy_dataset_path = os.path.abspath("../application_programming_l2/copy_dataset")
    path_to_files1 = third_script.get_path_to_files(copy_dataset_path)
    third_script.write_as_csv(copy_dataset_path, path_to_files1)
    mark = 4
    path_to_folder = path + f'/{mark}'
    num_of_files = sum(os.path.isfile(os.path.join(path_to_folder, f))
                        for f in os.listdir(path_to_folder)) + 1
    for id in range(1,num_of_files):
        print(fourth_script.get_next_exemplar(mark, id))