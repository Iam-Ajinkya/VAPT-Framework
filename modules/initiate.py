import json
import logging

def run():
    logging.info("Initiating VAPT process")
    with open('config/config.json', 'r') as file:
        config = json.load(file)
    with open('scope.json', 'w') as file:
        json.dump(config, file)
    logging.info("Scope defined and authorization obtained")

if __name__ == "__main__":
    run()
