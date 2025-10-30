"""Inventory Management System
This module provides functionality to add, remove, load, save, and check
inventory items. It uses JSON for storage and logging for activity tracking.
"""

import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='inventory.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Global variable
stock_data = {}


def add_item(item=None, qty=0, logs=None):
    """Add an item and quantity to stock_data with validation."""
    if logs is None:
        logs = []
    if not isinstance(item, str) or not isinstance(qty, (int, float)):
        logging.warning("Invalid item or quantity type: %s, %s", item, qty)
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info("Added %d of %s", qty, item)


def remove_item(item, qty):
    """Remove a quantity of an item from stock_data."""
    if item not in stock_data:
        logging.warning("Attempted to remove non-existing item: %s", item)
        return
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
            logging.info("Removed item completely: %s", item)
    except (KeyError, TypeError) as error:
        logging.error("Error removing item %s: %s", item, error)


def get_qty(item):
    """Return the quantity of a given item."""
    return stock_data.get(item, 0)


def load_data(file_path="inventory.json"):
    """Load inventory data from JSON file."""
    global stock_data
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            stock_data = json.load(file)
            logging.info("Data loaded from %s", file_path)
    except FileNotFoundError:
        logging.warning("File not found: %s", file_path)
    except (json.JSONDecodeError, IOError) as error:
        logging.error("Error loading data from %s: %s", file_path, error)


def save_data(file_path="inventory.json"):
    """Save inventory data to JSON file."""
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(stock_data, file, indent=4, ensure_ascii=False)
            logging.info("Data saved to %s", file_path)
    except (IOError, OSError) as error:
        logging.error("Error saving data: %s", error)


def print_data():
    """Print current inventory in a formatted manner."""
    print("\nItems Report:")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return items with quantity below the threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main function to test inventory operations."""
    add_item("apple", 10)
    add_item("banana", 2)
    add_item("orange", 1)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()
