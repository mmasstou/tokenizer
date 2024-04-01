from tokenizer import Tokenizer

# Example usage
tokenizer = Tokenizer()
text = """Many words map to one token, but some don't: indivisible.

Unicode characters like emojis may be split into many tokens containing the underlying bytes: 🤚🏾

Sequences of characters commonly found next to each other may be grouped together: 1234567890"""
tokens = tokenizer.tokenize(text)
print(f"tokens IDs : {tokens}")
token_length = len(tokens)
print(f"tokens : {token_length}")
