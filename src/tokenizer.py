from transformers import AutoTokenizer

def get_tokenizer(model_name):
    return AutoTokenizer.from_pretrained(model_name)

def tokenize_and_align_labels(example, tokenizer, label2id):
    tokenized = tokenizer(example["tokens"], is_split_into_words=True, truncation=True)
    word_ids = tokenized.word_ids()
    labels = []
    prev_word_id = None
    for word_id in word_ids:
        if word_id is None:
            labels.append(-100)
        elif word_id != prev_word_id:
            labels.append(label2id[example["labels"][word_id]])
        else:
            labels.append(label2id[example["labels"][word_id]])
        prev_word_id = word_id
    tokenized["labels"] = labels
    return tokenized
