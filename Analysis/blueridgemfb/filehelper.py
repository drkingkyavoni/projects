#!/usr/bin/python3

import os
from csv import DictReader, DictWriter
from dataclasses import dataclass, field
from typing import Callable, Generator, Optional, Tuple


@dataclass
class Output:
    header: list[str] = field(init=False)
    size: int = 0
    path: str = ""


_out: Output = Output()


def process_file(
    f: Callable[
        [
            DictReader,
        ],
        Tuple[Optional[Generator[dict, None, None]], Optional[Exception]],
    ],
    base: str,
    filename: str,
) -> Tuple[Optional[Generator[dict, None, None]], Optional[Exception]]:
    """
    Asynchronously processes a file using the provided function and returns the content along with any potential exceptions.

    Parameters:
        f (Callable): The function used to process the file.
        base (str): The base directory for the file.
        filename (str): The name of the file to be processed.

    Returns:
        Tuple[Generator[dict, None, None] | None, Exception | None]: A tuple containing the content generated from processing the file and any potential exceptions.
    """

    try:
        with open(os.path.join(base, filename), "r", encoding="utf-8") as inputFile:
            reader: DictReader = DictReader(inputFile)
            content, err = f(reader)

        _out.path = os.path.join(base, f"{f.__name__[4:]}.csv")
        return (content, err)
    except Exception as e:
        return (None, e)


def write_file(
    content: Generator[dict, None, None],
) -> Tuple[Optional[Output], Optional[Exception]]:
    """
    Asynchronously writes content to a file and returns a tuple containing the output or None, and the exception or None.
    """
    try:
        if _out.path == "":
            raise ValueError("Empty path")

        with open(_out.path, "w", encoding="utf-8") as outfile:
            writer: DictWriter = DictWriter(outfile, fieldnames=_out.header)
            writer.writeheader()
            writer.writerows(content)

        _out.size = os.stat(_out.path).st_size
        return (_out, None)
    except Exception as e:
        return (None, e)