def extract_letters(word):
    letters = ''

    for i in range(len(word)):
        if not word[i].isdigit():
            letters += word[i]
    return letters

def sum_digits(word):
    total = 0
    for i in range(len(word)):
        if word[i].isdigit():
            total += int(word[i])
    return total

def rotate_word(word, positions):
    positions = positions % len(word)
    rotated = word[positions:] + word[:positions]
    return rotated

def decode_word(word):
    letters = extract_letters(word)
    positions = sum_digits(word)
    has_digits = False

    for i in range(len(word)):
        if word[i].isdigit():
            has_digits = True
    if has_digits:
        return rotate_word(letters, positions)
    else:
        return letters

def main():
    message = input('Enter a secret message: ')
    words = message.split()
    decoded_words = []
    modified = 0
    digit_words = 0

    for i in range(len(words)):
        decoded = decode_word(words[i])
        decoded_words.append(decoded)

        if decoded != words[i]:
            modified += 1

        has_digits = False

        for j in range(len(words[i])):
            if words[i][j].isdigit():
                has_digits = True
        if has_digits:
            digit_words += 1
    message = ' '.join(decoded_words)
    print(f'Decoded message: {message}')
    print(f'Total words modified: {modified}')
    print(f'Words containing digits: {digit_words}')

main()
