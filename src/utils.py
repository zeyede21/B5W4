import numpy as np
import evaluate

def build_label_maps(y_train):
    label_list = sorted(set(label for doc in y_train for label in doc))
    label2id = {l: i for i, l in enumerate(label_list)}
    id2label = {i: l for l, i in label2id.items()}
    return label_list, label2id, id2label

def compute_metrics(id2label):
    metric = evaluate.load("seqeval")
    def compute(p):
        predictions, labels = p
        predictions = np.argmax(predictions, axis=2)
        true_labels = [
            [id2label[l] for l in label if l != -100]
            for label in labels
        ]
        true_predictions = [
            [id2label[p] for p, l in zip(pred, label) if l != -100]
            for pred, label in zip(predictions, labels)
        ]
        return metric.compute(predictions=true_predictions, references=true_labels)
    return compute
