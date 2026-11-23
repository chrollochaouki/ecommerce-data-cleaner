# E-commerce Data Cleaner

A Python script that cleans raw e-commerce order data: it takes a messy CSV and outputs a validated, deduplicated one.

## Problem

Real-world order data is dirty — missing prices, invalid values, duplicates. Feeding that into analytics or a warehouse corrupts every downstream result. This script validates and cleans it first.

## What it does

Reads a raw orders CSV and keeps only valid rows, rejecting:
- non-numeric prices (e.g. empty or "invalid")
- prices ≤ 0
- quantities ≤ 0
- rows with an empty customer email
- exact duplicate orders

Outputs a clean CSV and a short report (rows read / kept / rejected).

## How to run

```bash
python3 clean_orders.py
```

Input: `orders_raw.csv` · Output: `orders_clean.csv`

## Design

Structured as a simple ETL pipeline with three functions:
- `load()` — read the CSV (Extract)
- `clean()` — apply validation rules (Transform)
- `save()` — write the clean CSV (Load)

## Tech

Python 3, standard `csv` module. No external dependencies.