import random
import os 
import shutil
import csv


class Review:
    def __init__(self):
        self.name = None
        self.review = None
        self.mark = None


def create_folder():
    os.mkdir("copy_dataset")
    for i in range(1,6):
        os.mkdir("copy_dataset/" + str(i))


def get_dataset(path):
    dataset = list()
    for num_of_folder in range(1,6):
        path_to_folder = os.path.join(path, str(num_of_folder))
        num_of_files = sum(os.path.isfile(os.path.join(path_to_folder, f))
                           for f in os.listdir(path_to_folder)) + 1
        for i in range(1,num_of_files):
            path_to_file = os.path.join(path_to_folder, f"{(i):04}.txt")
            file = open(path_to_file, mode="r", encoding="utf-8")
            print(f"{num_of_folder}:{(i):04}")
            review = Review
            #
            dataset.append(review)
    return dataset


def create_copy(path):
    dataset = get_dataset(path)
    create_folder
