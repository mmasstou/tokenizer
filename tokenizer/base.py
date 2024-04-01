from tiktoken import encoding_for_model

__all__ = ["Tokenizer"]


class Tokenizer:
    def __init__(self, model_name: str = "gpt-4") -> None:
        """
        Initializes a Tokenizer instance using the specified model for encoding.

        Args:
            model_name (str, optional): Name of the GPT model to use for encoding.
                Defaults to "gpt-4". Check tiktoken documentation or the OpenAI API
                for available models.

        Raises:
            ValueError: If the specified model is not found in the available encodings.
        """
        try:
            self.encoding = encoding_for_model(model_name)
        except ValueError as e:
            raise ValueError(
                f"Invalid model name: {model_name}. Supported models: {', '.join(encoding_for_model.supported_models())}"
            ) from e

    def tokenize(self, text: str) -> list:
        """
        Tokenizes the provided text string using the chosen model's encoding.

        Args:
            text (str): The text string to tokenize.

        Returns:
            list: A list of tokens representing the tokenized text.
        """
        return self.encoding.encode(text)
