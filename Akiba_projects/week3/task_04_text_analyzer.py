
paragraph = input("Enter your paragraph.")


def clean_text(paragraph):
    cleaned = paragraph.lower()
    words = cleaned.split()

    cleaned_words = []

    for word in words:
        word = word.strip(".,!?;:")
        if word != "":
            cleaned_words.append(word)

    return cleaned_words


def count_word(paragraph):
    words = clean_text(paragraph)
    word_count = 0

    for word in words:
        word_count += 1

    return word_count


def char_count(paragraph):
    text_no_space = paragraph.replace(" ", "")

    count = len(text_no_space)

    return count


def count_vowels_consonants(paragraph):
    paragraph = paragraph.lower()
    vowels = 0
    consonants = 0

    for character in paragraph:
        if character in "aeiou":
            vowels += 1
        elif character in "bcdfghjklmnpqrstvwxyz":
            consonants += 1

    return vowels, consonants


def longest_word(paragraph):
    words = clean_text(paragraph)

    if len(words) == 0:
        return None

    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


def word_frequency(paragraph):
    words = clean_text(paragraph)
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


def repeated_words(paragraph):
    frequency = word_frequency(paragraph)

    repeated = []

    for word in frequency:
        if frequency[word] > 1:
            repeated.append(word)

    return repeated


def five_most_frequent_words(paragraph):
    frequency = word_frequency(paragraph)
    top_words = []

    for i in range(5):
        if len(frequency) == 0:
            break

        most_frequent = max(frequency, key=frequency.get)
        top_words.append((most_frequent, frequency[most_frequent]))

        del frequency[most_frequent]

    return top_words


def analyze_text(paragraph):
    vowels, consonants = count_vowels_consonants(paragraph)

    report = {
        "Word count": count_word(paragraph),
        "Character count (excluding spaces)": char_count(paragraph),
        "Vowels": vowels,
        "Consonants": consonants,
        "Longest word": longest_word(paragraph),
        "Word frequencies": word_frequency(paragraph),
        "Repeated words": repeated_words(paragraph),
        "Five most frequent words": five_most_frequent_words(paragraph)
    }

    return report


result = analyze_text(paragraph)

print("     --TEXT ANALYSIS REPORT--  ")

for item in result:
    print(item + ":", result[item])
