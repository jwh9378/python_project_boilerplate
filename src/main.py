import logging

import GlobalConfigs  # noqa: F401


def hello_world() -> str:
    return "Hello, World!"


def main() -> None:
    """Entry point for the hypermodern Python application."""
    logging.debug("""
                  Debugging information.
                  Useful for diagnosing problems.
                  """)
    logging.info("This is a hypermodern Python application.")
    logging.warning("This is a warning message.")
    logging.error("An error has occurred.")
    logging.critical("Critical issue encountered.")


if __name__ == "__main__":
    main()
