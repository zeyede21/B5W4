from transformers import AutoModelForTokenClassification

def get_model(model_name, num_labels, label2id, id2label):
    return AutoModelForTokenClassification.from_pretrained(
        model_name,
        num_labels=num_labels,
        label2id=label2id,
        id2label=id2label
    )
