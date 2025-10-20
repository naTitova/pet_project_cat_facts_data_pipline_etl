import requests
import csv
import logging
from datetime import datetime

#Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s -%(message)s")

API_URL = "https://catfact.ninja/fact"
CSV_PATH = "data/catfacts.csv"

def get_cat_fact():
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()

def save_to_csv(fact_data):
    with open(CSV_PATH, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), fact_data["fact"], fact_data["length"]])

def main():
    logging.info("Starting CatFacts ETL...)")
    try:
        for i in range(10): #laden 10 Fakten
            fact = get_cat_fact()
            save_to_csv(fact)
            logging.info(f"Saved fact #{i+1}")
        logging.info("ETL finished successfully")
    except Exception as e:
        logging.error(f"Error during ETL:{e}")
        
if __name__=="__main__":
    main()
        
    