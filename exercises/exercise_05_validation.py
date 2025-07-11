"""
Exercise 5: Response Validation
Your task: Implement AI-powered response validation
"""

import openai
import requests
import json
from config import OPENAI_API_KEY


class ResponseValidator:
    def __init__(self, api_key):
        self.client = openai.OpenAI(api_key=api_key)

    def validate_response_structure(self, response_data, expected_structure):
        """
        TODO: Validate API response structure using AI

        Args:
            response_data: Actual API response
            expected_structure: Expected response structure

        Returns:
            Dict with validation results
        """
        # TODO: Create validation prompt
        # TODO: Make API call
        # TODO: Parse validation results

        return {
            "is_valid": False,
            "issues": ["TODO: Implement structure validation"]
        }

    def detect_anomalies(self, response_data):
        """
        TODO: Use AI to detect anomalies in API responses

        Args:
            response_data: API response to analyze

        Returns:
            List of detected anomalies
        """
        # TODO: Create anomaly detection prompt
        # TODO: Make API call
        # TODO: Parse anomalies

        return ["TODO: Implement anomaly detection"]


def main():
    print("=== Exercise 5: Response Validation ===")

    validator = ResponseValidator(OPENAI_API_KEY)

    # Get sample response
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    response_data = response.json()

    print(f"API Response: {json.dumps(response_data, indent=2)}")

    # Expected structure
    expected_structure = {
        "userId": "integer",
        "id": "integer",
        "title": "string",
        "body": "string"
    }

    # TODO: Validate structure
    validation_results = validator.validate_response_structure(response_data, expected_structure)

    print(f"\nValidation Results:")
    print(f"Valid: {validation_results['is_valid']}")
    if validation_results['issues']:
        print("Issues found:")
        for issue in validation_results['issues']:
            print(f"  - {issue}")

    # TODO: Detect anomalies
    anomalies = validator.detect_anomalies(response_data)

    print(f"\nAnomalies Detected:")
    for anomaly in anomalies:
        print(f"  - {anomaly}")


if __name__ == "__main__":
    main()
