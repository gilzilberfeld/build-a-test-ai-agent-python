import google.genai as genai
from google.genai import types
from config import GEMINI_API_KEY
import ast

class HelloWorldCodeGenAgent:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
        self.model_name = 'gemini-1.5-flash-latest'
        self.config = types.GenerateContentConfig(max_output_tokens=100)

    def generate_hello_function(self):
        prompt = (
            "Generate a Python function named 'hello_name' that takes a parameter 'name' and returns the string 'Hello, {name}!'. "
            "Return ONLY the function code, no explanation."
        )
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=[types.Content(role="user", parts=[types.Part.from_text(text=prompt)])],
            config=self.config
        )
        code = response.text.strip().replace("```python", "").replace("```", "")
        return code

def validate_code(code):
    try:
        ast.parse(code)
        if 'def hello_name' not in code:
            return False, "Missing required function definition"
        return True, "Code validation passed"
    except SyntaxError as e:
        return False, f"Syntax error: {str(e)}"
    except Exception as e:
        return False, f"Validation error: {str(e)}"

def validate_function_output(func, name):
    expected = f"Hello, {name}!"
    result = func(name)
    if result == expected:
        return True, "Function output validation passed"
    else:
        return False, f"Function returned '{result}', expected '{expected}'"

def main():
    print("=== Demo: Generate, Validate, and Test Hello World Function ===")
    agent = HelloWorldCodeGenAgent(GEMINI_API_KEY)
    name = "Gil"
    code = agent.generate_hello_function()
    print("Generated function code:\n")
    print(code)
    is_valid, message = validate_code(code)
    if not is_valid:
        print(f"\n❌ Code validation failed: {message}")
        return
    print("\n✅ Code validation passed!")
    exec_globals = {}
    exec(code, exec_globals)
    func = exec_globals['hello_name']
    output_valid, output_message = validate_function_output(func, name)
    if output_valid:
        print("✅ Function output validation passed!")
    else:
        print(f"❌ {output_message}")
    print("Function output:")
    print(func(name))

if __name__ == "__main__":
    main()