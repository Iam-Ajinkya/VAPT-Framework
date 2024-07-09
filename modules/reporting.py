import json
import logging

def generate_report():
    report = {
        "findings": [
            {"vulnerability": "Sample vulnerability", "impact": "High", "recommendation": "Fix it"}
        ]
    }
    with open('report.json', 'w') as file:
        json.dump(report, file)
    logging.info("Report generated")

def run():
    logging.info("Reporting started")
    generate_report()
    logging.info("Reporting completed")

if __name__ == "__main__":
    run()
