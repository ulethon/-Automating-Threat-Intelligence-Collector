import requests
import json
import csv

class ThreatCollector:
    def __init__(self, api_key, source_url="https://api.example.com"):
        self.api_key = api_key
        self.source_url = source_url
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def collect_data(self):
        """Collects threat intelligence data from an external API"""
        response = requests.get(f"{self.source_url}/threats", headers=self.headers)
        if response.status_code == 200:
            self.data = response.json()
            print("Data collected successfully.")
        else:
            print(f"Failed to collect data: {response.status_code}")
            self.data = []

    def generate_report(self, output="report.csv"):
        """Generates a CSV report from the collected data"""
        if not self.data:
            print("No data to generate a report.")
            return
        
        # Write data to CSV
        with open(output, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Threat Type", "Description", "Date"])
            for threat in self.data:
                writer.writerow([threat["id"], threat["type"], threat["description"], threat["date"]])
        print(f"Report generated: {output}")

if __name__ == "__main__":
    collector = ThreatCollector(api_key="YOUR_API_KEY")
    collector.collect_data()
    collector.generate_report("threat_report.csv")
