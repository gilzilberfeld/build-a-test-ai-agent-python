"""
Solution 6: Complete API Test Agent - Full Implementation
"""

import requests
import json
import time
import google.genai as genai
from google.genai import types
from config import GEMINI_API_KEY
from utils.sample_apis import SAMPLE_ENDPOINTS


class APITestAgent:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
        self.test_results = []
        self.model_name = 'gemini-1.5-flash-latest'
        self.config = types.GenerateContentConfig(max_output_tokens=400)

    def analyze_endpoint(self, endpoint_info):
        """Analyze a single endpoint"""
        prompt = f"""
        Analyze this API endpoint briefly:
        Method: {endpoint_info['method']} 
        Path: {endpoint_info['path']}

        In 1-2 sentences, describe what this endpoint does and its main purpose.
        """

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=[
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text = "You are an API analyst. Be concise.")]
                ),
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text = prompt)]
                )
            ],
            config=self.config
        )

        return response.text

    def generate_test_for_endpoint(self, endpoint_info):
        """Generate test code for an endpoint"""
        prompt = f"""
        Generate a simple Python test for this endpoint:
        Method: {endpoint_info['method']}
        Path: {endpoint_info['path']}
        Base URL: https://jsonplaceholder.typicode.com

        Create a function called 'test_endpoint' that:
        1. Makes the API call
        2. Returns a dict with 'success', 'status_code', 'response_time'
        3. Uses try/except for error handling

        Return ONLY the Python function code.
        """

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=[
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text = "Generate clean, executable Python test code.")]
                ),
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text = prompt)]
                )
            ],
            config=self.config
        )

        # Remove the python code wrapper
        code = response.text.strip().replace("```python", "").replace("```", "")

        # Clean up the response to remove any code block formatting
        return code

    def execute_test_code(self, test_code):
        """Execute test code and return results"""
        try:
            exec_globals = {
                'requests': requests,
                'json': json,
                'time': time
            }

            exec(test_code, exec_globals)

            if 'test_endpoint' in exec_globals:
                result = exec_globals['test_endpoint']()
                return {
                    "execution_success": True,
                    "test_result": result
                }
            else:
                return {
                    "execution_success": False,
                    "error": "No test_endpoint function found"
                }

        except Exception as e:
            return {
                "execution_success": False,
                "error": str(e)
            }

    def run_complete_analysis(self, api_endpoints):
        """
        Run complete analysis workflow for multiple endpoints
        """
        results = {
            "total_endpoints": len(api_endpoints),
            "tests_run": 0,
            "successful_tests": 0,
            "failed_tests": 0,
            "endpoint_results": []
        }

        for endpoint in api_endpoints:
            print(f"\n🔍 Analyzing {endpoint['method']} {endpoint['path']}...")

            # Step 1: Analyze endpoint
            analysis = self.analyze_endpoint(endpoint)

            # Step 2: Generate test code
            print("💡 Generating test code...")
            test_code = self.generate_test_for_endpoint(endpoint)

            # Step 3: Execute test
            print("🚀 Executing test...")
            execution_result = self.execute_test_code(test_code)

            # Step 4: Collect results
            endpoint_result = {
                "endpoint": f"{endpoint['method']} {endpoint['path']}",
                "analysis": analysis,
                "test_executed": execution_result["execution_success"],
                "test_result": execution_result.get("test_result", {}),
                "error": execution_result.get("error")
            }

            results["endpoint_results"].append(endpoint_result)

            if execution_result["execution_success"]:
                results["tests_run"] += 1
                test_success = execution_result.get("test_result", {}).get("success", False)
                if test_success:
                    results["successful_tests"] += 1
                    print("✅ Test passed!")
                else:
                    results["failed_tests"] += 1
                    print("❌ Test failed!")
            else:
                print(f"⚠️  Test execution failed: {execution_result.get('error')}")

        # Calculate success rate
        if results["tests_run"] > 0:
            results["success_rate"] = results["successful_tests"] / results["tests_run"]
        else:
            results["success_rate"] = 0.0

        return results

    def generate_executive_summary(self, test_results):
        """Generate executive summary using AI"""
        prompt = f"""
        Generate an executive summary for these API test results:

        Total Endpoints: {test_results['total_endpoints']}
        Tests Run: {test_results['tests_run']}
        Successful Tests: {test_results['successful_tests']}
        Failed Tests: {test_results['failed_tests']}
        Success Rate: {test_results['success_rate']:.1%}

        Detailed Results:
        {json.dumps(test_results['endpoint_results'], indent=2)}

        Provide:
        1. Overall assessment
        2. Key findings
        3. Any concerns or recommendations
        4. Next steps

        Keep it concise and business-focused.
        """

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=[
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text = "You are an expert test analyst creating executive summaries.")]
                ),
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text = prompt)]
                )
            ],
            config=self.config
        )

        return response.text


def main():
    print("=== Solution 6: Complete API Test Agent ===")

    agent = APITestAgent(GEMINI_API_KEY)

    # Use sample endpoints
    endpoints = SAMPLE_ENDPOINTS[0]["endpoints"][:3]  # First 3 endpoints

    print(f"Testing {len(endpoints)} endpoints...")
    print("=" * 60)

    # Run complete analysis
    results = agent.run_complete_analysis(endpoints)

    print("\n" + "=" * 60)
    print("🎉 ANALYSIS COMPLETE!")
    print("=" * 60)

    print(f"\nTest Results Summary:")
    print(f"Endpoints analyzed: {results['total_endpoints']}")
    print(f"Tests executed: {results['tests_run']}")
    print(f"Successful tests: {results['successful_tests']}")
    print(f"Failed tests: {results['failed_tests']}")
    print(f"Success rate: {results['success_rate']:.1%}")

    # Generate executive summary
    print("\n" + "=" * 60)
    print("📊 EXECUTIVE SUMMARY")
    print("=" * 60)
    summary = agent.generate_executive_summary(results)
    print(summary)


if __name__ == "__main__":
    main()