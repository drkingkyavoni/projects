#!/usr/bin/python3
import csv
import os


def find_multiple_files(source):
    return [file for file in os.listdir(source) if file.endswith(".csv")]

def count_number_of_records(path, csvFiles):
    """
    Counts the number of records in the given CSV files located at the specified path.

    Args:
        path (str): The path where the CSV files are located.
        csvFiles (list): List of CSV file names to be processed.

    Returns:
        int: The total number of records across all CSV files.
    """
    count = 0
    for file in csvFiles:
        print(os.path.join(path, file))
        with open(os.path.join(path, file), mode="r", encoding="utf-8") as csvFile:
            reader = csv.DictReader(csvFile)
            count += len(list(reader)) if reader else 0
    return count

def count_blank_first_names(path, csvFiles):
    """
    Counts the number of blank first names in the CSV files located at the given path.

    Args:
        path (str): The path to the directory containing the CSV files.
        csvFiles (list): A list of CSV file names.

    Returns:
        int: The count of blank first names in the CSV files.
    """
    count = 0
    for file in csvFiles:
        print(os.path.join(path, file))
        with open(os.path.join(path, file), mode="r", encoding="utf-8") as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                if row["first_name"] == "":
                    count += 1
    return count

if __name__ == "__main__":
    path = "/mnt/c/PSMD/OPay Audit/Evidence/cbn-user/"
    csvFiles = find_multiple_files(path)
    # print("Total number of records: {:>,}".format(
    #     count_number_of_records(path, csvFiles)))
    print("Number of blank first names: {:>,}".format(
        count_blank_first_names(path, csvFiles)))