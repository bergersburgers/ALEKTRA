# main.py

import requests  # Library for making HTTP requests
import json      # For pretty-printing or saving JSON data
from datetime import date  # For working with dates

# -------------------------------
# Configuration: API Endpoints
# -------------------------------

# Base URLs for MISO APIs
PRICING_BASE = "https://apim.misoenergy.org/pricing/v1/day-ahead"
LGI_BASE = "https://apim.misoenergy.org/lgi/v1/day-ahead"

# -------------------------------
# Helper Function to Pull Data
# -------------------------------

def get_miso_pricing(market_date: str, interval=None, pageNumber=None, product=None, zone=None):
    """
    Pulls Day-Ahead pricing data from MISO
    :param market_date: YYYY-MM-DD
    :param interval: optional, e.g., "13" or "13:05"
    :param pageNumber: optional pagination
    :param product: optional, e.g., "Regulation", "Spin"
    :param zone: optional, e.g., "Zone 1"
    """
    url = f"{PRICING_BASE}/{market_date}/asm-exante"
    
    # Build query params dictionary
    params = {}
    if interval:
        params["interval"] = interval
    if pageNumber:
        params["pageNumber"] = pageNumber
    if product:
        params["product"] = product
    if zone:
        params["zone"] = zone

    response = requests.get(url, params=params)
    response.raise_for_status()  # Throw error if request fails
    return response.json()       # Return parsed JSON data


def get_miso_lgi(market_date: str, interval=None, pageNumber=None, region=None):
    """
    Pulls Load, Generation, and Interchange (LGI) data from MISO
    """
    url = f"{LGI_BASE}/{market_date}/interchange/net-scheduled"

    params = {}
    if interval:
        params["interval"] = interval
    if pageNumber:
        params["pageNumber"] = pageNumber
    if region:
        params["region"] = region

    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

# -------------------------------
# Example Usage
# -------------------------------

if __name__ == "__main__":
    # Get today's date in YYYY-MM-DD format
    today = date.today().isoformat()

    # Pull pricing data for all zones, all products
    pricing_data = get_miso_pricing(today)
    print("Pricing Data Sample:")
    print(json.dumps(pricing_data[:2], indent=2))  # Print first 2 entries for clarity

    # Pull LGI data for all regions
    lgi_data = get_miso_lgi(today)
    print("\nLGI Data Sample:")
    print(json.dumps(lgi_data[:2], indent=2))
