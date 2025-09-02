class PromptManager:
    def __init__(self, prompt_file):
        self.prompt_file = prompt_file
        self._prompt = None

    def load_prompt(self):
        if self._prompt is None:
            with open(self.prompt_file, 'r') as f:
                self._prompt = f.read()
        return self._prompt

    def get_prompt(self):
        return self.load_prompt()
