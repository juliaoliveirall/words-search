def words(file_path):
    with open(file_path, 'r') as file:
        words = [line.strip().upper() for line in file if line.strip() and not line.startswith('#')]
    return words

words = words('words.txt')
print(words)
