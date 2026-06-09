from pathlib import Path
import torch

PROJECT_DIR = Path(__file__).resolve().parent
print(PROJECT_DIR)
words = open(PROJECT_DIR/'names.txt', 'r').read().splitlines()
chars = sorted(list(set(''.join(words))))
chtoi = {ch:i  for i,ch in enumerate(chars)}
chtoi['<s>']=26
chtoi['<e>']=27
itoch = {i:ch for ch,i in chtoi.items()}

N = torch.zeros((28, 28), dtype=torch.int32)


for word in words:
    chs = ['<s>'] + list(word) + ['<e>']
    for ch1,ch2 in zip(chs, chs[1:]):
        x1 = chtoi[ch1]
        x2 = chtoi[ch2]
        N[x1, x2] +=1
        
print(N)

import matplotlib.pyplot as plt
plt.figure(figsize=(16,16))
plt.imshow(N, cmap="Blues")

for i in range(28):
    for j in range(28) :
        ctstr = itoch[i] + itoch[j]
        

