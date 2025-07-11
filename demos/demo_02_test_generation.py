"""
Demo 2: Test Idea Generation - Shows how AI can generate test scenarios
"""

import openai
from config import OPENAI_API_KEY


class TestIdeaGenerator:
    def __init__(self, api_key):
        self.client = openai.OpenAI(api_key=api_key)

    def generate_test_ideas(self, api_description):
        """Generate test ideas for an API"""
        prompt = f"""
        API Description: {api_description}

        Generate 5 different test scenarios for this API. For each test, provide:
        1. Test name
        2. What it tests
        3. Expected result

        Format as a numbered list.
        """

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert API tester."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300
        )
        return response.choices[0].message.content


def main():
    print("=== Test Idea Generation Demo ===")

    generator = TestIdeaGenerator(OPENAI_API_KEY)

    # Simple API description
    api_description = "GET /users/{id} - Returns user information including name, email, and registration date"

    print(f"API: {api_description}")
    print("\nGenerating test ideas...")

    ideas = generator.generate_test_ideas(api_description)
    print(f"\nTest Ideas:\n{ideas}")


if __name__ == "__main__":
    main()
