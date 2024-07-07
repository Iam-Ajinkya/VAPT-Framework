import json
import subprocess
import logging

def passive_info_gathering(targets, tools):
    for target in targets:
        try:
            result = subprocess.run([tools['whois'], target], capture_output=True, text=True)
            logging.info(f"Passive info gathering for {target}: {result.stdout}")
        except Exception as e:
            logging.error(f"Error during passive info gathering for {target}: {e}")

def active_info_gathering(targets, tools):
    for target in targets:
        try:
            result = subprocess.run([tools['nmap'], "-sP", target], capture_output=True, text=True)
            logging.info(f"Active info gathering for {target}: {result.stdout}")
        except Exception as e:
            logging.error(f"Error during active info gathering for {target}: {e}")

def run():
    logging.info("Reconnaissance started")
    with open('scope.json', 'r') as file:
        scope = json.load(file)
    passive_info_gathering(scope["targets"], scope["tools"])
    active_info_gathering(scope["targets"], scope["tools"])
    logging.info("Reconnaissance completed")

if __name__ == "__main__":
    run()
