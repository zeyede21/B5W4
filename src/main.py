from data_loader import prepare_datasets
from tokenizer import get_tokenizer, tokenize_and_align_labels
from utils import build_label_maps, compute_metrics
from model import get_model
from trainer import get_training_args, get_trainer

def main():
    conll_path = "../labeled/labeled.conll"
    model_name = "Davlan/bert-base-multilingual-cased-ner-hrl"
    output_dir = "../ner-amharic-model"

    # Load and prepare data
    train_data, test_data, y_train = prepare_datasets(conll_path)

    # Label maps
    label_list, label2id, id2label = build_label_maps(y_train)

    # Tokenizer
    tokenizer = get_tokenizer(model_name)

    # Tokenize
    train_data = train_data.map(lambda x: tokenize_and_align_labels(x, tokenizer, label2id))
    test_data = test_data.map(lambda x: tokenize_and_align_labels(x, tokenizer, label2id))

    # Model
    model = get_model(model_name, len(label_list), label2id, id2label)

    # Training
    training_args = get_training_args(output_dir)
    trainer = get_trainer(model, training_args, train_data, test_data, tokenizer, compute_metrics(id2label))
    
    trainer.train()
    trainer.save_model(output_dir)
    tokenizer.save_pretrained(output_dir)

if __name__ == "__main__":
    main()
