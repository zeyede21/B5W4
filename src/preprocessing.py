import pandas as pd
import re

# ---------------------------------------
# Text cleaning & tokenization function
# ---------------------------------------
def clean_text(text):
    if not isinstance(text, str):
        return ""

    # Remove emojis
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # Emoticons
        "\U0001F300-\U0001F5FF"  # Symbols & pictographs
        "\U0001F680-\U0001F6FF"  # Transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # Flags
        "]+",
        flags=re.UNICODE
    )
    text = emoji_pattern.sub(r"", text)

    # Remove URLs
    text = re.sub(r"http\S+|www\S+|t\.me/\S+", "", text)

    # Remove usernames, hashtags
    text = re.sub(r"@\S+|#\S+", "", text)

    # Remove special characters (except Amharic characters, numbers, and punctuation)
    text = re.sub(r"[^\u1200-\u137F\u1380-\u139F\u2D80-\u2DDF\uAB00-\uAB2F\u200c\u200d፡።፣፤0-9A-Za-z\s]", " ", text)

    # Normalize spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text

def tokenize_text(text):
    return text.split()  # Simple whitespace tokenizer

def process_text(text):
    cleaned = clean_text(text)
    tokens = tokenize_text(cleaned)
    return tokens

# ---------------------------------------
# Main preprocessing pipeline
# ---------------------------------------
def main(input_file="../data/telegram_scraped_messages.csv", output_file="../data/tokenized_messages.csv"):
    # Load raw message data
    df = pd.read_csv(input_file)

    if "text" not in df.columns:
        raise ValueError("The input CSV must have a 'message' column.")

    # Apply preprocessing
    df["tokens"] = df["text"].apply(lambda x: process_text(str(x)))

    # Save processed data
    df.to_csv(output_file, index=False)
    print(f"Tokenized messages saved to {output_file}")

if __name__ == "__main__":
    main()
