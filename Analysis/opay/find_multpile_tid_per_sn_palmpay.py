#!/usr/bin/python3

import csv
import os
import pathlib


def find_duplicate(filePath):
    """
    Function to find duplicate values in a CSV file based on a specific column.

    Args:
        filePath (str): The path to the directory containing the CSV file.
        columnName (str): The name of the column to check for duplicate values.

    Returns:
        int: 1 if duplicate values are found, 0 if no duplicate values are found.
    """

    base_file = f"{filePath}/pos_param_config_ng_terminal_info_collection_202401301124.csv"
    print(f"Reading file: {base_file}")

    """
    Read the csv file
    For each row, create a content dictionary with the key of 'serial' and
    value as a list of 'terminal_id'
    """
    content = {}
    with open(base_file, mode='r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            content.setdefault(
                row['Device SN'],
                []).append(row['Virtual Terminal ID'])

    """
    For each row in the content dictionary, check if the length of values
    in the dictionary value is greater than 1
    then append the record to a filtered dictionary
    """
    filtered = {
        key: sorted(value) for key, value in content.items()
        if len(value) > 1
    }

    """
    Write the filtered dictionary to a new csv file
    Return 1 if the write is successful, 0 if not
    """
    print("Total number of duplicate records: {:>,}".format(len(filtered)))
    if not len(filtered):
        return 0

    with open(f"{filePath}/multpile_tid_per_sn.csv", mode='w',
              encoding='utf-8') as csv_file:
        fieldnames = ['Device SN', 'count', 'Virtual Terminal ID']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for key, value in filtered.items():
            writer.writerow({
                'Device SN': key,
                'count': len(value),
                'Virtual Terminal ID': value
            })

    return 1 if os.stat(f"{filePath}/multpile_tid_per_sn.csv") else 0

if __name__ == '__main__':
    folder = pathlib.Path('/mnt/c/PSMD/PalmPay/Evidences/pos/')
    print("Write to file {}".format("successful"
            if find_duplicate(folder)
            else "failed"
            ))