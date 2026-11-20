
from prometheus_client import Counter, Gauge, generate_latest, start_http_server
import time

delivery_requests = Counter(
    'delivery_requests_total',
    'Total number of delivery requests'
)

pending_deliveries = Gauge(
    'pending_deliveries',
    'Number of pending deliveries'
)

def update_metrics():
    delivery_requests.inc()
    pending_deliveries.set(5)

def get_metrics():
    return generate_latest().decode('utf-8')

if __name__ == "__main__":
    start_http_server(8000)
    print("Delivery Metrics Exporter running on port 8000")

    while True:
        update_metrics()
        time.sleep(5)
