# Delivery Metrics Exporter

A Python-based Prometheus metrics exporter.

## Features

- Tracks total delivery requests.
- Tracks pending deliveries.
- Exposes metrics on port 8000.

## Installation

pip install -r requirements.txt

## Run Application

python metrics_exporter.py

## Metrics Endpoint

http://localhost:8000/metrics

## Run Tests

python -m unittest test_metrics -v