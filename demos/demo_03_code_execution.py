"""
Demo 3: Code Execution - Shows how to run generated code safely
"""

import requests
import json


def simple_api_test():
    """A simple API test that we'll run"""
    print("Running simple API test...")

    # Test a simple GET request
    url = "https://httpbin.org/get"
    response = requests.get(url)

    result = {
        "status_code": response.status_code,
        "success": response.status_code == 200,
        "response_time": response.elapsed.total_seconds(),
        "data_received": len(response.text) > 0
    }

    print(f"Test Results: {json.dumps(result, indent=2)}")
    return result


def main():
    print("=== Code Execution Demo ===")

    # Run our test
    result = simple_api_test()

    # Analyze results
    if result["success"]:
        print("\n✅ Test PASSED!")
    else:
        print("\n❌ Test FAILED!")

    print(f"Response time: {result['response_time']:.2f} seconds")


if __name__ == "__main__":
    main()
