from src.config_manager import ConfigManager
import requests


class LLMManager:
    def __init__(self, llm_url, llm_model, prompt_file):
        self.llm_url = llm_url
        self.llm_model = llm_model
        self.prompt_file = prompt_file

    def call_llm(self, message, extra_context=None):
        payload = {
            "model": self.llm_model,
            "message": message
        }
        if extra_context:
            payload["context"] = extra_context
        response = requests.post(self.llm_url, json=payload)
        return response.json()

    def get_prompt(self):
        if self.prompt_file:
            with open(self.prompt_file, 'r') as f:
                return f.read()
        return ""
