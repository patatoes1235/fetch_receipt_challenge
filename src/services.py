
from datetime import time
from .schemas import Receipt


points_dict:dict[str, int] = {}

def calculate_points(receipt: Receipt):
    """
    Calculate the points earned for a receipt.
    Rules:
        1 point for every alphanumeric character in the retailer name.
        50 points if the total is a round dollar amount with no cents.
        25 points if the total is a multiple of 0.25.
        5 points for every two items on the receipt.
        If the trimmed length of the item description is a multiple of 3, multiply the price by 0.2 and round up to the nearest integer. The result is the number of points earned.
        6 points if the day in the purchase date is odd.
        10 points if the time of purchase is after 2:00pm and before 4:00pm.
    """
    total_points = 0
    alphanum_chars = sum([c.isalnum() for c in receipt.retailer])
    total_points += alphanum_chars

    if receipt.total.is_integer():
        total_points += 50
    if receipt.total % 0.25 == 0:
        total_points += 25
    total_points += (len(receipt.items) // 2) * 5

    for item in receipt.items:
        if len(item.desc.strip()) % 3 == 0:
            total_points += int(item.price * 0.2 + 1) # round up
    
    if receipt.purchaseDate.day % 2 == 1:
        total_points += 6
    
    if receipt.purchaseTime > time(14, 0) and receipt.purchaseTime < time(16, 0):
        total_points += 10

    return total_points

def validate_receipt(receipt: Receipt):
    """
    Validate the receipt data. Raises a ValueError if the receipt is invalid.
    """
    if len(receipt.items) < 1:
        raise ValueError("Receipt does not contain any items.")
    if receipt.total < 0:
        raise ValueError("Total amount on receipt is negative.")
    
    item_total = 0
    for item in receipt.items:
        if item.price < 0:
            raise ValueError("Item price is negative.")
        item_total += item.price
    
    if item_total != receipt.total:
        raise ValueError("Total amount on receipt does not match sum of item prices.")
    