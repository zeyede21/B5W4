from transformers import Trainer, TrainingArguments

def get_training_args(output_dir):
    return TrainingArguments(
        output_dir=output_dir,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        num_train_epochs=5,
        weight_decay=0.01,
        logging_dir="./logs",
        logging_strategy="steps",
        logging_steps=10,
        report_to="none"
    )

def get_trainer(model, args, train_data, test_data, tokenizer, compute_metrics):
    return Trainer(
        model=model,
        args=args,
        train_dataset=train_data,
        eval_dataset=test_data,
        tokenizer=tokenizer,
        compute_metrics=compute_metrics
    )
