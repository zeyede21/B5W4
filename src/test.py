import pandas as pd

df = pd.read_csv("../data/tokenized_messages.csv")
sample = df[['tokens']].dropna().sample(40, random_state=42)
sample.to_csv("../data/ner_sample.csv", index=False, encoding='utf-8')
print("✅ Exported 40 messages to ner_sample.csv")
