import re

R_SPECIAL_CHAR = re.compile(r'\W+')
R_WHITESPACE = re.compile(r'\s{2,}')


def _remove_special_characters(text):
    """
    Remove special characters and converts text to lowercase.

    Args:
        text (str): The text to clean.

    Returns:
        str: The cleaned text.
    """
    return re.sub(R_SPECIAL_CHAR, ' ', text)


def _remove_whitespaces(text):
    """
    Remove whitespaces from text.

    Args:
        text (str): The text to remove whitespaces from.

    Returns:
        str: The cleaned text.
    """
    return re.sub(R_WHITESPACE, ' ', text)


def clean_text(text):
    """
    Remove special characters from text.
    Removes duplicate whitespace from text.
    Removes leading / trailing whitespace from text.

    Args:
        text (str): The text to clean.

    Returns:
        str: The cleaned text.
    """
    return _remove_whitespaces(_remove_special_characters(text)).strip()
