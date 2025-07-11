"""
Solution 3: Test Code Generation - Complete Implementation
"""

import openai
import ast
from config import OPENAI_API_KEY


class TestCodeGenerator:
    def __init__(self, api_key):
        self.client = openai.OpenAI(api_key=api_key)

    def generate_test_function(self, test_description, endpoint_info):
        """
        Generate executable Python test code
        """
        prompt = f"""
        Generate a Python test function for this scenario:

        Test Description: {test_description}
        API Method: {endpoint_info['method']}
        API Path: {endpoint_info['path']}
        Base URL: {endpoint_info.get('base_url', 'https://jsonplaceholder.typicode.com')}

        Requirements:
        - Use the requests library
        - Create a function named 'test_api_endpoint'
        - Include proper error handling with try/except
        - Return a dictionary with test results including:
          * 'success': boolean
          * 'status_code': HTTP status code
          * 'response_time': response time in seconds
          * 'error': error message if any
          * 'data': response data if successful
        - Include assertions where appropriate
        - Handle timeouts (set timeout=10)

        Return ONLY the Python function code, no explanation.
        """

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "You are an expert Python developer. Generate clean, executable test code."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500
        )

        return response.choices[0].message.content

    def validate_generated_code(self, code):
        """
        Validate that generated code is syntactically correct
        """
        try:
            # Try to parse the code
            ast.parse(code)

            # Check for required elements
            required_elements = ['def test_api_endpoint', 'import requests', 'return']
            missing_elements = []

            for element in required_elements:
                if element not in code:
                    missing_elements.append(element)

            if missing_elements:
                return False, f"Missing required elements: {', '.join(missing_elements)}"

            return True, "Code validation passed"

        except SyntaxError as e:
            return False, f"Syntax error: {str(e)}"
        except Exception as e:
            return False, f"Validation error: {str(e)}"


def main():
    print("=== Solution 3: Test Code Generation ===")

    generator = TestCodeGenerator(OPENAI_API_KEY)

    # Test scenario
    test_description = "Test that GET /posts/1 returns a valid post with required fields (id, title, body, userId)"
    endpoint = {
        "method": "GET",
        "path": "/posts/1",
        "description": "Get specific post",
        "base_url": "https://jsonplaceholder.typicode.com"
    }

    print(f"Generating code for: {test_description}")

    # Generate test code
    code = generator.generate_test_function(test_description, endpoint)

    print(f"\nGenerated Code:")
    print("=" * 50)
    print(code)
    print("=" * 50)

    # Validate the code
    is_valid, error = generator.validate_generated_code(code)

    if is_valid:
        print("\n✅ Code validation passed!")

        # Try to execute the code to show it works
        try:
            exec_globals = {
                'requests': __import__('requests'),
                'json': __import__('json'),
                'time': __import__('time')
            }
            exec(code, exec_globals)
            result = exec_globals['test_api_endpoint']()
            print(f"\nTest execution result: {result}")
        except Exception as e:
            print(f"\nNote: Code generated but execution failed: {e}")
    else:
        print(f"\n❌ Code validation failed: {error}")


if __name__ == "__main__":
    main()
