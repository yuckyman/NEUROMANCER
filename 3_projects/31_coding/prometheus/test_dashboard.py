#!/usr/bin/env python3
"""
test script for prometheus dashboard
verifies that the dashboard is working correctly
"""

import requests
import json
import time
import sys

def test_dashboard():
    """test the dashboard endpoints"""
    base_url = "http://localhost:12345"
    
    print("🧪 testing prometheus dashboard...")
    
    # test main dashboard
    try:
        response = requests.get(f"{base_url}/", timeout=5)
        if response.status_code == 200 and "Prometheus Market Intelligence" in response.text:
            print("✅ dashboard page loaded")
        else:
            print(f"❌ dashboard page failed: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ dashboard page error: {e}")
        return False
    
    # test api endpoint
    try:
        response = requests.get(f"{base_url}/api/data", timeout=5)
        if response.status_code == 200:
            data = response.json()
            if 'market_data' in data and 'predictions' in data:
                print("✅ api endpoint working")
                print(f"📊 found data for {len(data['market_data'])} symbols")
            else:
                print("❌ api endpoint returned invalid data")
                return False
        else:
            print(f"❌ api endpoint failed: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ api endpoint error: {e}")
        return False
    
    print("🎉 all tests passed! dashboard is working correctly")
    return True

if __name__ == "__main__":
    success = test_dashboard()
    sys.exit(0 if success else 1)
