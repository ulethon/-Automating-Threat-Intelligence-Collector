import unittest
from threat_intelligence_collector.collector import ThreatCollector

class TestThreatCollector(unittest.TestCase):

    def setUp(self):
        self.collector = ThreatCollector(api_key="test_api_key")

    def test_collect_data_success(self):
        self.collector.collect_data()
        self.assertIsInstance(self.collector.data, list)
        self.assertGreater(len(self.collector.data), 0)

    def test_generate_report(self):
        self.collector.collect_data()
        self.collector.generate_report("test_report.csv")
        with open("test_report.csv", "r") as file:
            lines = file.readlines()
            self.assertGreater(len(lines), 1)

if __name__ == "__main__":
    unittest.main()
