# your code goes here!
# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        # Sort the original word once for comparison
        sorted_original = sorted(self.word)
        matches = []

        for word in word_list:
            # Skip exact same word (optional depending on test)
            if word.lower() == self.word:
                continue

            if sorted(word.lower()) == sorted_original:
                matches.append(word)

        return matches
