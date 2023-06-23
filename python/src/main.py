#!/usr/bin/env python3

def main() -> None:
    """
    Simply the main function.
    """

    print("Hello, world!")


if __name__ == "__main__":
    try:
        main()

    except (EOFError, KeyboardInterrupt):
        pass
