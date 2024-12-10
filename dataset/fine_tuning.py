from transformers import BartTokenizer, BartForConditionalGeneration, Trainer, TrainingArguments, EarlyStoppingCallback
from datasets import load_dataset
import pandas as pd

# Load tokenizer and model for BART
tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")

# Load the dataset
dataset = pd.read_csv("automotive_text_summarize.csv")  # Pastikan file berada di direktori yang sama

# Save the dataset as a temporary CSV file
dataset.to_csv("data_di_train.csv", index=False)

# Load the dataset using load_dataset
train_dataset = load_dataset('csv', data_files='data_di_train.csv', split='train')

# Preprocess the dataset
def preprocess_function(examples):
    inputs = [doc for doc in examples["Text"]]
    model_inputs = tokenizer(inputs, max_length=1024, padding=True, truncation=True)  # Added padding=True

    # Setup the tokenizer for targets
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(examples["Summarize"], max_length=128, padding=True, truncation=True)  # Added padding=True

    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

tokenized_train = train_dataset.map(preprocess_function, batched=True)

# Define training arguments
training_args = TrainingArguments(
    output_dir="./results",
    eval_strategy="no",  # No evaluation dataset
    save_strategy="epoch",  # Save model at the end of each epoch
    learning_rate=3e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    weight_decay=0.01,
    save_total_limit=3,
    num_train_epochs=5,
    logging_dir='./logs',
    logging_steps=500,  # Log every 500 steps
)

# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_train,
    tokenizer=tokenizer
)

# Train the model
trainer.train()

# Save the trained model and tokenizer
model.save_pretrained("fine_tuned_BART")
tokenizer.save_pretrained("fine_tuned_BART")
print("Model and tokenizer saved successfully!")
