import random
# função usada para ler e carregar as palavras escritas no txt
def read_words(file_path = 'words.txt'):
    with open(file_path, 'r') as file:
        return [line.strip().upper() for line in file if line.strip() and not line.startswith('#')]
    
# função usada para criar uma matriz vazia
def crate_matriz(size):
    return [[' ' for _ in range(size)] for _ in range(size)]

