# 🐱 CatFacts Data Pipeline

A small Python ETL project that collects random cat facts from [catfact.ninja](https://catfact.ninja/fact)  
and saves them into a CSV file for further analysis.

## Features

- Fetches 10 random facts via REST API
- Saves results with timestamp and length
- Uses logging for process tracking

## Tech Stack

- Python 3.10+
- requests
- csv
- logging

## How to run

```bash
pip install -r requirements.txt
python src/main.py
