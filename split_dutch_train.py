# Take the data from Data/train_dutch.txt, and randomly take 10% of the lines and save them to Data/val_dutch.txt,
# then remove those lines from Data/train_dutch.txt

import random

print("Splitting data...")
# Read the data from the file
with open("Data/train_dutch.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Randomly shuffle the lines
random.shuffle(lines)

# Take 10% of the lines
num_lines = len(lines)
num_val = int(num_lines * 0.1)
val_lines = lines[:num_val]
train_lines = lines[num_val:]

print(f"Number of lines in val: {num_val}")
# Write the validation data to the val file
with open("Data/val_dutch.txt", "w", encoding="utf-8") as file:
    for line in val_lines:
        file.write(line)

print(f"Number of lines in train: {len(train_lines)}")
# Write the training data to the train file
with open("Data/train_dutch.txt", "w", encoding="utf-8") as file:
    for line in train_lines:
        file.write(line)

print("Done!")