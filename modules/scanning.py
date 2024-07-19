import json
import subprocess
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

def parallel_vulnerability_scanning(targets, tools):
    scan_results = {}
    with ThreadPoolExecutor() as executor:
        futures = []
        for target in targets:
            futures.append(executor.submit(run_scan, target, tools))

        for future in as_completed(futures):
            target, result = future.result()
            scan_results[target] = result

    return scan_results

def run_scan(target, tools):
    try:
        result = subprocess.run(
            [tools['nmap'], "-sV", "--script=vuln", target, "-T4"],
            capture_output=True,
            text=True,
            timeout=300
        )
        logging.info(f"Vulnerability scanning for {target} completed")
        return target, result.stdout
    except subprocess.TimeoutExpired:
        logging.error(f"Vulnerability scanning for {target} timed out")
    except Exception as e:
        logging.error(f"Error during vulnerability scanning for {target}: {e}")
    return target, ""

def run():
    logging.info("Scanning started")
    with open('scope.json', 'r') as file:
        scope = json.load(file)

    scan_results = parallel_vulnerability_scanning(scope["targets"], scope["tools"])

    with open('scan_results.json', 'w') as file:
        json.dump(scan_results, file)

    logging.info("Scanning completed")

if __name__ == "__main__":
    run()
