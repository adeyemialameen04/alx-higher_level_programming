#!/usr/bin/python3
"""Documenting module"""


def print_stats(size, stats_codes):
    """
    This function prints the metrics
    """
    print("File size: {}".format(size))
    for key in sorted(stats_codes):
        print("{}: {}".format(key, stats_codes[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    allowed_codes = ['200', '301', '400', '401', '403',
                     '404', '405', '500']
    line_count = 0

    try:
        for read_line in sys.stdin:
            if line_count == 10:
                print_stats(size, status_codes)
                line_count = 1
            else:
                line_count += 1

            read_line = read_line.split()

            try:
                size += int(read_line[-1])
            except (IndexError, ValueError):
                pass

            try:
                code = read_line[-2]
                if code in allowed_codes:
                    if status_codes.get(code, -1) == -1:
                        status_codes[code] = 1
                    else:
                        status_codes[code] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
