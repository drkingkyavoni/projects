#!/usr/bin/python3

from csv import DictReader
from typing import Generator, Optional, Tuple


def get_blank_nin(
    dictreader: DictReader,
) -> Tuple[Optional[Generator[dict, None, None]], Optional[Exception]]:
    """
    Asynchronous function to get a generator of dictionaries with a blank "nin" field from a DictReader.

    Args:
        dictreader (DictReader): The input dictionary reader.

    Returns:
        Tuple[Optional[Generator[dict, None, None]], Optional[Exception]]: A tuple containing the generator of dictionaries with a blank "nin" field and any raised exception, if any.
    """
    try:
        result = (row for row in dictreader if row["nin"] == "")
        return result, None
    except Exception as e:
        return None, e


def get_blank_bvn(
    dictreader: DictReader,
) -> Tuple[Optional[Generator[dict, None, None]], Optional[Exception]]:
    """
    Asynchronous function to get the blank BVN from the given DictReader.

    Args:
        dictreader (DictReader): The dictionary reader.

    Returns:
        Tuple[Generator[dict, None, None] | None, Exception | None]: A tuple containing the generator of dictionaries with blank BVN and any raised exception.
    """
    try:
        result = (row for row in dictreader if row["bvn"] == "")
        return result, None
    except Exception as e:
        return None, e


def get_blank_bvn_nin(
    dictreader: DictReader,
) -> Tuple[Optional[Generator[dict, None, None]], Optional[Exception]]:
    """
    An asynchronous function that takes a DictReader as input and returns a tuple containing a generator of dictionaries or None, and an exception or None.
    """
    try:
        result = (row for row in dictreader if row["bvn"] == "" and row["nin"] == "")
        return result, None
    except Exception as e:
        return None, e


def get_duplicate_bvn(
    dictreader: DictReader,
) -> Tuple[Optional[Generator[dict, None, None]], Optional[Exception]]:
    """
    Asynchronous function to get duplicate bvn.

    Args:
        dictreader: A DictReader object.

    Returns:
        A tuple containing a generator of dictionaries or None, and an exception or None.
    """
    try:
        result = (row for row in dictreader if row["nin"] == "")
        return result, None
    except Exception as e:
        return None, e


def get_blank_name(
    dictreader: DictReader,
) -> Tuple[Optional[Generator[dict, None, None]], Optional[Exception]]:
    """
    An asynchronous function that takes a DictReader as input and returns a tuple containing a generator of dictionaries or None, and an exception or None.
    """
    try:
        result = (row for row in dictreader if row["name"] == "")
        return result, None
    except Exception as e:
        return None, e


def get_blank_address(
    dictreader: DictReader,
) -> Tuple[Optional[Generator[dict, None, None]], Optional[Exception]]:
    """
    Asynchronous function to get a blank address. Takes a DictReader as input. Returns a tuple containing a generator of dictionaries plus None, or an Exception plus None.
    """
    try:
        result = (row for row in dictreader if row["nin"] == "")
        return result, None
    except Exception as e:
        return None, e


def get_invalid_dob(
    dictreader: DictReader,
) -> Tuple[Optional[Generator[dict, None, None]], Optional[Exception]]:
    """
    Asynchronous function to get invalid date of birth from a dictionary reader.

    Args:
        dictreader (DictReader): The dictionary reader object.

    Returns:
        Tuple[Generator[dict, None, None] | None, Exception | None]: A tuple containing a generator of invalid date of birth dictionaries or None, and an exception or None.
    """
    try:
        result = (row for row in dictreader if row["dob"] == "")
        return result, None
    except Exception as e:
        return None, e