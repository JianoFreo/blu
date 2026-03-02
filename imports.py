import torch

with open('wizard_of_oz.txt', 'r', encoding='utf-8') as f:
    text = f.read()

chars = sorted(set(text))

string_to_int = { ch:i for i,ch in enumerate(chars) }  # maps each character to a unique integer
int_to_string = { i:ch for i,ch in enumerate(chars) }  # maps each integer back to its character
encode = lambda string: [string_to_int[char] for char in string]
decode = lambda Integer: ''.join([int_to_string[i] for i in Integer])

data = torch.tensor(encode(text), dtype=torch.long)

n = int(0.8 * len(data))
train_data = data[:n]
val_data = data[n:]
