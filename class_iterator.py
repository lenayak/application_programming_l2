import os
from typing import Optional


class SimpleIterator:
    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.counter = 0

    def __get_next__(self, mark) -> Optional[str]:
        if self.counter >= self.limit:
            return None
        self.counter += 1
        return os.path.abspath("../application_programmind_l1/dataset" + f"/{mark}" + f"/{self.counter:04}.txt")

    def __next__(self) -> Optional[str]:
        if self.counter < self.limit:
            self.counter += 1
            return 1
        else:
            raise StopIteration


if __name__ == "__main__":
    mark = 4
    path = os.path.abspath("../application_programming_l1/dataset")
    path_to_folder = path + f"/{mark}"
    num_of_files = sum(os.path.isfile(os.path.join(path_to_folder, f))
                        for f in os.listdir(path_to_folder)) + 1
    iter = SimpleIterator(num_of_files)
    for i in range(1, num_of_files):
        print(iter.__get_next__(mark))