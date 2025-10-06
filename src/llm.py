# import libraries
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # Loads environment variables from .env
token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-mini"
# A function to call an LLM model and return the response
def call_llm_model(model, messages, temperature=1.0, top_p=1.0):
    client = OpenAI(base_url=endpoint,api_key=token)
    response = client.chat.completions.create(
    messages=messages,
    temperature=temperature, top_p=top_p, model=model)
    return response.choices[0].message.content
# A function to translate to target language
def translate_to_language(text, target_language):
    prompt = f"Translate the following text to {target_language}:\n\n{text}"
    messages = [{"role": "user", "content": prompt}]
    return call_llm_model(model, messages)
# Run the main function if this script is executed
if __name__ == "__main__":
    sample_text = "Hello, how are you?"
    target_language = "chinese"
    translated_text = translate_to_language(sample_text, target_language)
    print(f"Original text: {sample_text}")
    print(f"Translated text: {translated_text}")