import subprocess
import logging
import json
from modules import initiate, reconnaissance, scanning, manual_testing, exploitation, post_exploitation, reporting, review_and_mitigation, retesting

# Setup logging
logging.basicConfig(filename='logs/vapt.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("VAPT Framework started")
    try:
        initiate.run()
        reconnaissance.run()
        scanning.run()
        manual_testing.run()
        exploitation.run()
        post_exploitation.run()
        reporting.run()
        review_and_mitigation.run()
        retesting.run()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    logging.info("VAPT Framework completed")

if __name__ == "__main__":
    main()
