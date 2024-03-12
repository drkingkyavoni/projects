import hashlib
from pathlib import Path

csv_files = []
txt_files = []


def compare_fileHash():
    filePath = "/mnt/c/OFISD/OneDrive_1_1-5-2024/"
    for child in Path(filePath).rglob("*"):
        if child.suffix == ".csv":
            csv_files.append(child)
        if child.suffix == ".txt":
            txt_files.append(child)

    for csv_file, txt_file in zip(csv_files, txt_files):
        with open(txt_file, mode="r", encoding="utf-8") as txt, open(
            csv_file, mode="rb"
        ) as csv:
            txt_content = txt.read()
            csv_content = csv.read()

            # Calculate MD5 hash of CSV file content
            csv_hash = hashlib.md5(csv_content).hexdigest()

            if txt_content == csv_hash:
                print("Hash matches. {}".format(csv_file))
            else:
                print(
                    "Hash NOT Matched {} != {} {}".format(
                        txt_content, csv_hash, csv_file
                    )
                )


if __name__ == "__main__":
    compare_fileHash()
