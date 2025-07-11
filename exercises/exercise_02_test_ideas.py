"""
Exercise 2: Test Idea Generation
Your task: Generate comprehensive test ideas for API endpoints
"""

import openai
from config import OPENAI_API_KEY
from utils.sample_apis import SAMPLE_ENDPOINTS


class TestIdeaGenerator:
    def __init__(self, api_key):
        self.client = openai.OpenAI(api_key=api_key)

    def generate_test_categories(self, endpoint_info):
        """
        TODO: Generate different categories of tests

        Categories to consider:
        - Happy path tests
        - Error handling tests
        - Edge cases
        - Security tests
        - Performance tests

        Returns:
            Dict with test categories and ideas
        """
        # TODO: Create comprehensive prompt
        # TODO: Make API call
        # TODO: Parse response into categories

        return {
            "happy_path": ["TODO: Implement happy path tests"],
            "error_handling": ["TODO: Implement error tests"],
            "edge_cases": ["TODO: Implement edge case tests"]
        }

    def prioritize_tests(self, test_ideas):
        """
        TODO: Use AI to prioritize which tests to run first

        Args:
            test_ideas: Dict of test categories and ideas

        Returns:
            List of prioritized test ideas
        """
        # TODO: Create prioritization prompt
        # TODO: Make API call
        # TODO: Return prioritized list

        return ["TODO: Implement test prioritization"]


def main():
    print("=== Exercise 2: Test Idea Generation ===")

    generator = TestIdeaGenerator(OPENAI_API_KEY)

    # Use a more complex endpoint
    endpoint = SAMPLE_ENDPOINTS[0]["endpoints"][1]  # GET /posts/1

    print(f"Generating test ideas for: {endpoint['method']} {endpoint['path']}")

    # TODO: Generate test categories
    test_ideas = generator.generate_test_categories(endpoint)

    print("\nTest Ideas by Category:")
    for category, ideas in test_ideas.items():
        print(f"\n{category.upper()}:")
        for idea in ideas:
            print(f"  - {idea}")

    # TODO: Prioritize tests
    prioritized = generator.prioritize_tests(test_ideas)

    print("\nPrioritized Test Order:")
    for i, test in enumerate(prioritized, 1):
        print(f"{i}. {test}")


if __name__ == "__main__":
    main()
