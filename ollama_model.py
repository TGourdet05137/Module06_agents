# ollama_model.py
# Author: Tatyana Gourdet


from ollama import ResponseError, chat


class OllamaModel:
    """A real AI model that runs on this computer through Ollama."""

    def __init__(self, model_name):
        """Remember which model to ask."""
        self.model_name = model_name

    def reply(self, instructions, history):
        """Send the instructions and history to the model and return its reply."""
        messages = [{"role": "system", "content": instructions}] + history
        try:
            response = chat(model=self.model_name, messages=messages)
            return response.message.content
        except ConnectionError:
            return None
        except ResponseError:
            return None
        return response.message.content
