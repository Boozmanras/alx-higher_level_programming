#!/usr/bin/python3
"""Script to parse stdin and compute metrics.

Metrics:
- Total file size
- Number of lines by status code
"""


def main():
    """Read stdin line by line
       and compute metrics."""
    import sys

    total_size = 0
    status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            parts = line.split()
            if len(parts) < 7:
                continue
            status = parts[-2]
            size = parts[-1]
            if status in status_codes:
                status_codes[status] += 1
            try:
                total_size += int(size)
            except ValueError:
                pass

            if count % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    if count % 10 != 0:
        print_stats(total_size, status_codes)


def print_stats(total_size, status_codes):
    """Print the current metrics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == '__main__':
    main()
