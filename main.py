from stats import generate_report
import sys


def main():
    try:
        if len(sys.argv) != 2:
            raise Exception("Usage: python3 main.py <path_to_book>")
        generate_report(sys.argv[1])
    except Exception as e:
        print(e)
        sys.exit(1)

main()