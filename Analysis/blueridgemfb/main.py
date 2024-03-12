#!/usr/bin/python3

import os
from concurrent.futures import ProcessPoolExecutor, as_completed

import exceptions as ex
import filehelper as fh


def main() -> None:
    base: str = ""
    files: tuple = tuple(os.listdir(base))

    with ProcessPoolExecutor() as executor:
        futures = (
            executor.submit(fh.process_file, ex.get_blank_address, base, file)
            for file in files
        )

        content = [future.result() for future in as_completed(futures)]

        fh.write_file(content)


if __name__ == "__main__":
    main()