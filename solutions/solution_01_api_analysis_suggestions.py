"""
Solution 1: API Analysis Agent - exercises 1.1 and 1.2
"""

import google.genai as genai
from google.genai import types
from config import GEMINI_API_KEY
from utils.sample_apis import get_sample_api


class APIAnalysisAgent:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
        self.model_name = 'gemini-1.5-flash-latest'
        self.config = types.GenerateContentConfig(max_output_tokens=200)

    def analyze_api_endpoint(self, endpoint_info):
        """
        Analyze an API endpoint and understand its purpose
        """
        prompt = f"""
        Analyze this API endpoint and explain what it does:

        Method: {endpoint_info['method']}
        Path: {endpoint_info['path']}
        Description: {endpoint_info['description']}

        Provide a concise analysis of:
        1. What this endpoint does
        2. What data it likely returns
        3. Common use cases
        4. Potential issues to test for

        Keep response under 150 words.
        """
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=[
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text = "You are an expert API analyst focused on testing scenarios.")]
                ),
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text = prompt)]
                )
            ],
            config=self.config
        )
        return response.text

    def get_testing_suggestions(self, endpoint_info):
        """
        Generate specific testing suggestions for an endpoint
        """
        prompt = f"""
        Generate 5 specific test scenarios for this API endpoint:

        Method: {endpoint_info['method']}
        Path: {endpoint_info['path']}
        Description: {endpoint_info['description']}

        For each test, provide just the test name in this format:
        1. Test name here
        2. Test name here
        etc.

        Focus on practical tests that would catch real issues.
        """
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=[
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text = "You are an expert API tester. Generate practical test scenarios.")]
                ),
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text = prompt)]
                )
            ],
            config=self.config
        )

        # Parse response.text into list
        suggestions = []
        for line in response.text.split('\n'):
            if line.strip() and any(char.isdigit() for char in line[:5]):
                # Extract test name after number
                test_name = line.split('.', 1)[1].strip() if '.' in line else line.strip()
                suggestions.append(test_name)

        return suggestions[:5]  # Return max 5 suggestions


def main():
    print("=== Solution 1: API Analysis Agent ===")

    # Get sample API
    sample_api = get_sample_api()
    endpoint = sample_api["endpoints"][0]

    print(f"Analyzing endpoint: {endpoint['method']} {endpoint['path']}")

    # Create agent instance
    agent = APIAnalysisAgent(GEMINI_API_KEY)

    # Analyze the endpoint
    analysis = agent.analyze_api_endpoint(endpoint)
    print(f"\nAnalysis: {analysis}")

    # Get testing suggestions
    suggestions = agent.get_testing_suggestions(endpoint)
    print(f"\nTesting Suggestions:")
    for i, suggestion in enumerate(suggestions, 1):
        print(f"{i}. {suggestion}")


if __name__ == "__main__":
    main()
