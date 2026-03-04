#!/usr/bin/env python3
import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Reads data from a CSV file and converts it into a JSON file named data.json.
    Returns True if successful, False otherwise.
    """
    try:
        # 1. Read the CSV data
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            # DictReader uses the first row as dictionary keys
            reader = csv.DictReader(csv_file)
            data_list = [row for row in reader]

        # 2. Serialize and write to data.json
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except (FileNotFoundError, IOError, PermissionError):
        # Return False if the file is missing or inaccessible
        return False
