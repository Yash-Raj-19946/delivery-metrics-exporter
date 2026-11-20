
import unittest

from metrics_exporter import update_metrics, get_metrics


class TestMetricsExporter(unittest.TestCase):

    def test_metrics_generation(self):

        update_metrics()

        result = get_metrics()

        self.assertIn(
            "delivery_requests_total",
            result
        )

        self.assertIn(
            "pending_deliveries",
            result
        )


if __name__ == "__main__":
    unittest.main()
