"""
Base App

"""
import logging
from dotenv import load_dotenv

def init():
    load_dotenv()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    logging.info("Initializing applicaiton...")
    logging.info("Loaded environment variables")


def main():
    logging.info("Running application..")


if __name__ == "__main__":
    init()
    main()

