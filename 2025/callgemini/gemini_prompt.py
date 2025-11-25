"""
Gemini API Prompt Program
Author: Chan Ming Man
"""

import google.generativeai as genai
import os
from typing import Optional


def configure_gemini(api_key: Optional[str] = None):
    """
    Configure the Gemini API with your API key.
    
    Args:
        api_key: Your Gemini API key. If not provided, will look for GEMINI_API_KEY environment variable.
    """
    if api_key is None:
        api_key = os.getenv('GEMINI_API_KEY')
        if api_key is None:
            raise ValueError(
                "API key not found. Please provide it as an argument or set GEMINI_API_KEY environment variable.\n"
                "Get your API key from: https://aistudio.google.com/app/apikey"
            )
    
    genai.configure(api_key=api_key)


def prompt_gemini(prompt: str, model_name: str = "gemini-2.5-flash") -> str:
    """
    Send a prompt to Gemini and get a response.
    
    Args:
        prompt: The text prompt to send to Gemini
        model_name: The model to use (default: gemini-2.5-flash)
    
    Returns:
        The generated response from Gemini
    """
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(prompt)
    return response.text


def interactive_mode():
    """
    Run an interactive chat session with Gemini.
    """
    print("=== Gemini Interactive Mode ===")
    print("Type 'quit' or 'exit' to end the session.\n")
    
    model = genai.GenerativeModel('gemini-2.5-flash')
    chat = model.start_chat(history=[])
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['quit', 'exit']:
            print("Goodbye!")
            break
        
        if not user_input:
            continue
        
        try:
            response = chat.send_message(user_input)
            print(f"\nGemini: {response.text}\n")
        except Exception as e:
            print(f"Error: {e}\n")


def main():
    """
    Main function demonstrating different ways to use the Gemini API.
    """
    # Configure the API (you can also pass the API key directly here)
    try:
        configure_gemini()
    except ValueError as e:
        print(f"Configuration Error: {e}")
        return
    
    print("Gemini API configured successfully!\n")
    
    # Example 1: Single prompt
    print("=== Example 1: Single Prompt ===")
    prompt = "Explain quantum computing in simple terms."
    print(f"Prompt: {prompt}")
    response = prompt_gemini(prompt)
    print(f"Response: {response}\n")
    
    # Example 2: Interactive mode
    print("\n=== Starting Interactive Mode ===")
    interactive_mode()


if __name__ == "__main__":
    main()
