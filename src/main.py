import logging

import GlobalConfigs  # noqa: F401

if __name__ == "__main__":
    logging.debug("""
                  Debugging information.
                  Useful for diagnosing problems.
                  """)
    logging.info("This is a hypermodern Python application.")
    logging.warning("This is a warning message.")
    logging.error("An error has occurred.")
    logging.critical("Critical issue encountered.")
