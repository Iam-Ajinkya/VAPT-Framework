import logging

def manual_test():
    logging.info("Performing manual testing")
    print("Perform manual testing here.")
    logging.info("Manual testing completed")

def run():
    logging.info("Manual testing started")
    manual_test()
    logging.info("Manual testing completed")

if __name__ == "__main__":
    run()
