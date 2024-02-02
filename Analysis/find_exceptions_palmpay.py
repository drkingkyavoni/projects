#!/usr/bin/python3

import csv
import os


def find_exceptions(base, filename, fields=[]):
    """
    A function to find exceptions in a given file based on specified fields and constraints.

    Parameters:
    - base: The base directory for the file.
    - filename: The name of the file to be checked.
    - fields: A list of field names to be used for finding exceptions (default is an empty list).
    - constraint: A list of constraints to be applied (default is an empty list).

    Returns:
    - A string indicating the status of the operation.
    """

    filePath = f"{base}/{filename}"
    print("\n\n{}\n\n".format("*" * 50))
    print("Checking if file is successful...")
    if not os.path.exists(filePath):
        return f"Empty file path: {filePath}"

    print("File path: {} exists".format(filePath))
    print("Reading file...")

    content = csv.DictReader(open(filePath))

    if content is None:
        return "File not found"

    header = ["member_id","wallet_name","wallet_number",
              "bvn","nin","member_status","mobile_money_account_tier",
              "date_open","dob","address","current_balance",
              "business_type","phone","gender","create_time"]

    print("File {} successfully read".format(filePath))

    outFile = f"{base}/{'_'.join(fields)}_exception_tier_other.csv"

    print("Attempting to write to {} ...".format(outFile))
    with open(outFile, mode="w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=header)
        writer.writeheader()

        if not fields:
            writer.writerows(content)
            return "Write all content to {} successful".format(outFile)

        for row in content:
            if all(row[field] == '' for field in fields) and row['mobile_money_account_tier'] not in ['TIER1', 'TIER2', 'TIER3']:
                writer.writerow(row)

    fileContent = csv.DictReader(open(outFile))
    print("{} has {:,} rows".format(outFile, len(list(fileContent))))

    return "Write content to {} is {}".format(outFile, "successful"
        if os.stat(outFile) else "failed")

if __name__ == "__main__":
    file = "individual_new_account_since_20231201.csv"
    root = "/mnt/c/PSMD/PalmPay/Evidences/individual/from dec 1 2023"
    print(find_exceptions(root, file, ['wallet_name']))
    print(find_exceptions(root, file, ['bvn']))
    print(find_exceptions(root, file, ['nin']))
    print(find_exceptions(root, file, ['dob']))
    print(find_exceptions(root, file, ['gender']))
    print(find_exceptions(root, file, ['address']))
    print(find_exceptions(root, file, ['bvn', 'nin']))
