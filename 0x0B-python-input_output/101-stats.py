#!/usr/bin/python3
"""Documenting a module"""
import sys


def print_stats(size, stats_codes):
    """
    Prints the stats
    Args:
        size: The size of total size of the file
        stats_codes: The status codes.
    Returns:
        Nothing.
    """
    print("File size: {}".format(size))
    for code, count in stats_codes:
        if count > 0:
            print("{}: {}".format(code, count))


if __name__ == "__main__":
    """
    Documenting main.
    """
    size = 0
    stats_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
                   404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            file_size = int(parts[-1])
            code = int(parts[-2])

            size += file_size

            if code in stats_codes:
                stats_codes[code] += 1

            if line_count % 10 == 0:
                print_stats(size, stats_codes)
    except KeyboardInterrupt:
        print_stats(size, stats_codes)
