"""
Exercise 3: Test Code Generation
Your task: Generate executable Python test code
"""

import openai
from config import OPENAI_API_KEY


class TestCodeGenerator:
    def __init__(self, api_key):
        self.client = openai.OpenAI(api_key=api_key)

    def generate_test_function(self, test_description, endpoint_info):
        """
        TODO: Generate executable Python test code

        Args:
            test_description: What the test should do
            endpoint_info: API endpoint details

        Returns:
            String containing executable Python code
        """
        # TODO: Create prompt for code generation
        # Include requirements:
        # - Use requests library
        # - Include assertions
        # - Handle errors
        # - Return results

        prompt = f"""
        Generate a Python test function for this scenario:

        Test Description: {test_description}
        API Endpoint: {endpoint_info['method']} {endpoint_info['path']}

        Requirements:
        - Use the requests library
        - Include proper error handling
        - Return test results as a dictionary
        - Include assertions where appropriate

        # TODO: Complete the prompt
        """

        # TODO: Make API call
        # TODO: Extract code from response

        return "# TODO: Implement code generation"

    def validate_generated_code(self, code):
        """
        TODO: Validate that generated code is syntactically correct

        Args:
            code: Generated Python code

        Returns:
            Tuple of (is_valid, error_message)
        """
        # TODO: Try to compile the code
        # TODO: Check for basic syntax errors
        # TODO: Return validation results

        return True, "TODO: Implement validation"


def main():
    print("=== Exercise 3: Test Code Generation ===")

    generator = TestCodeGenerator(OPENAI_API_KEY)

    # Test scenario
    test_description = "Test that GET /posts/1 returns a valid post with required fields"
    endpoint = {
        "method": "GET",
        "path": "/posts/1",
        "description": "Get specific post",
        "base_url": "https://jsonplaceholder.typicode.com"
    }

    print(f"Generating code for: {test_description}")

    # TODO: Generate test code
    code = generator.generate_test_function(test_description, endpoint)

    print(f"\nGenerated Code:\n{code}")

    # TODO: Validate the code
    is_valid, error = generator.validate_generated_code(code)

    if is_valid:
        print("\n✅ Code validation passed!")
    else:
        print(f"\n❌ Code validation failed: {error}")


if __name__ == "__main__":
    main()
