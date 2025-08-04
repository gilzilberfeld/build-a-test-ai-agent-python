"""
Solution 2: Test Idea Generation - Complete Implementation
"""

import google.genai as genai
from google.genai import types
from config import GEMINI_API_KEY
from utils.sample_apis import SAMPLE_ENDPOINTS


class TestIdeaGenerator:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
        self.model_name = 'gemini-1.5-flash-latest'
        self.config = types.GenerateContentConfig(max_output_tokens=400)

    def generate_test_categories(self, endpoint_info):
        """
        Generate different categories of tests for comprehensive coverage
        """
        prompt = f"""
        Generate comprehensive test ideas for this API endpoint:

        Method: {endpoint_info['method']}
        Path: {endpoint_info['path']}
        Description: {endpoint_info['description']}

        Provide test ideas in these categories:

        HAPPY_PATH: (2-3 tests for normal, successful scenarios)
        ERROR_HANDLING: (2-3 tests for error conditions)
        EDGE_CASES: (2-3 tests for boundary conditions)

        Format each section clearly with the category name and numbered tests.
        """
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=[
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text = "You are an expert API tester. Generate comprehensive test scenarios.")]
                ),
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text = prompt)]
                )
            ],
            config=self.config
        )
        content = response.text
        categories = {
            "happy_path": [],
            "error_handling": [],
            "edge_cases": []
        }

        current_category = None
        for line in content.split('\n'):
            line = line.strip()
            if 'HAPPY_PATH' in line.upper():
                current_category = 'happy_path'
            elif 'ERROR_HANDLING' in line.upper() or 'ERROR' in line.upper():
                current_category = 'error_handling'
            elif 'EDGE_CASES' in line.upper() or 'EDGE' in line.upper():
                current_category = 'edge_cases'
            elif line and current_category and any(char.isdigit() for char in line[:5]):
                # Extract test after number
                test_name = line.split('.', 1)[1].strip() if '.' in line else line.strip()
                categories[current_category].append(test_name)

        return categories

    def prioritize_tests(self, test_ideas):
        """
        Use AI to prioritize which tests to run first
        """
        all_tests = []
        for category, tests in test_ideas.items():
            for test in tests:
                all_tests.append(f"{test} ({category})")

        prompt = f"""
        Prioritize these API tests in order of importance (most important first):

        {chr(10).join([f"{i + 1}. {test}" for i, test in enumerate(all_tests)])}

        Consider:
        - Risk of failure impact
        - Likelihood of catching issues
        - Essential functionality

        Return just the prioritized list with numbers:
        1. Most important test
        2. Second most important test
        etc.
        """
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=[
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text = "You are an expert test prioritization specialist.")]
                ),
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text = prompt)]
                )
            ],
            config=self.config
        )

        # Parse prioritized tests
        prioritized = []
        for line in response.text.split('\n'):
            if line.strip() and any(char.isdigit() for char in line[:5]):
                test_name = line.split('.', 1)[1].strip() if '.' in line else line.strip()
                prioritized.append(test_name)

        return prioritized


def main():
    print("=== Solution 2: Test Idea Generation ===")

    generator = TestIdeaGenerator(GEMINI_API_KEY)

    # Use a more complex endpoint
    endpoint = SAMPLE_ENDPOINTS[0]["endpoints"][1]  # GET /posts/1

    print(f"Generating test ideas for: {endpoint['method']} {endpoint['path']}")

    # Generate test categories
    test_ideas = generator.generate_test_categories(endpoint)

    print("\nTest Ideas by Category:")
    for category, ideas in test_ideas.items():
        print(f"\n{category.upper().replace('_', ' ')}:")
        for idea in ideas:
            print(f"  - {idea}")

    # Prioritize tests
    prioritized = generator.prioritize_tests(test_ideas)

    print("\nPrioritized Test Order:")
    for i, test in enumerate(prioritized, 1):
        print(f"{i}. {test}")


if __name__ == "__main__":
    main()
