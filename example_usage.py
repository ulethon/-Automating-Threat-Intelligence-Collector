from threat_intelligence_collector.collector import ThreatCollector

# Create a ThreatCollector instance
collector = ThreatCollector(api_key="YOUR_API_KEY")

# Collect threat intelligence data
collector.collect_data()

# Generate a report with the collected data
collector.generate_report(output="my_threat_report.csv")
