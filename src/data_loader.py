from datasets import Dataset
from sklearn.model_selection import train_test_split

def load_conll(path):
    tokens, tags, temp = [], [], []
    with open(path, encoding='utf-8') as f:
        for line in f:
            if line.strip() == "":
                if temp:
                    sent, lbls = zip(*temp)
                    tokens.append(list(sent))
                    tags.append(list(lbls))
                    temp = []
            else:
                parts = line.strip().split()
                if len(parts) == 2:
                    word, tag = parts
                    temp.append((word, tag))
    return tokens, tags

def prepare_datasets(conll_path, test_size=0.1):
    tokens, tags = load_conll(conll_path)
    X_train, X_test, y_train, y_test = train_test_split(tokens, tags, test_size=test_size)
    train_data = Dataset.from_dict({"tokens": X_train, "labels": y_train})
    test_data = Dataset.from_dict({"tokens": X_test, "labels": y_test})
    return train_data, test_data, y_train
