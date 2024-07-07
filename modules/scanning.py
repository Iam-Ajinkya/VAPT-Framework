import json
import subprocess
import logging

def vulnerability_scanning(targets, tools):
    for target in targets:
        try:
            result = subprocess.run([tools['nmap'], "-sV", "--script=vuln", target], capture_output=True, text=True)
            logging.info(f"Vulnerability scanning for {target}: {result.stdout}")
        except Exception as e:
            logging.error(f"Error during vulnerability scanning for {target}: {e}")

def run():
    logging.info("Scanning started")
    with open('scope.json', 'r') as file:
        scope = json.load(file)
    vulnerability_scanning(scope["targets"], scope["tools"])
    logging.info("Scanning completed")

if __name__ == "__main__":
    run()
