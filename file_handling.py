# File Handling - Alex Mwirigi
# Nairobi, Kenya

import csv
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def create_sample_data():
    data = [
        ["name", "age", "income"],
        ["John", 25, 50000],
        ["Mary", 30, 75000],
        ["Peter", 22, 30000],
        ["Amina", 35, 90000]
    ]
    
    with open("sample_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)
    
    logging.info("Sample data created successfully")


def read_data():
    try:
        with open("sample_data.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        logging.error("Data file not found")

def process_data():
    try:
        with open("sample_data.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)  # skip header row
            total_income = 0
            count = 0
            for row in reader:
                total_income += int(row[2])
                count += 1
            average_income = total_income / count
            logging.info(f"Average income processed: {average_income}")
            return average_income
    except FileNotFoundError:
        logging.error("Data file not found")

process_data()

read_data()

create_sample_data()

