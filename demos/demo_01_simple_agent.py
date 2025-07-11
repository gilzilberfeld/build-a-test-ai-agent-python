"""
Demo 1: Simple AI Agent - Shows basic LLM interaction
Run this to understand how an AI agent thinks and responds
"""

import openai
from config import OPENAI_API_KEY


class SimpleAgent:
    def __init__(self, api_key):
        self.client = openai.OpenAI(api_key=api_key)

    def think(self, question):
        """Ask the AI to think about something"""
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful API testing assistant."},
                {"role": "user", "content": question}
            ],
            max_tokens=200
        )
        return response.choices[0].message.content


def main():
    print("=== Simple AI Agent Demo ===")

    # Create our simple agent
    agent = SimpleAgent(OPENAI_API_KEY)

    # Ask it to think about APIs
    question = "What should I test when I have a REST API that manages user posts?"

    print(f"Question: {question}")
    print("\nAgent thinking...")

    answer = agent.think(question)
    print(f"\nAgent says: {answer}")


if __name__ == "__main__":
    main()
