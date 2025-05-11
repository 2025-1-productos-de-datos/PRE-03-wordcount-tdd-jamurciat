import argparse
import os

from ._internals.count_words import count_words  # type: ignore
from ._internals.parse_args import parse_args  # type: ignore
from ._internals.preprocess_lines import preprocess_lines  # type: ignore
from ._internals.read_all_lines import read_all_lines  # type: ignore
from ._internals.split_into_words import split_into_words  # type: ignore
from ._internals.write_word_counts import write_word_counts  # type: ignore


def main():
    input_folder, output_folder = parse_args()
    lines = read_all_lines(input_folder)
    preprocessed_lines = preprocess_lines(lines)
    words = split_into_words(preprocessed_lines)
    word_counts = count_words(words)
    write_word_counts(output_folder, word_counts)
