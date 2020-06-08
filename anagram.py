#!/usr/bin/env python3
import argparse


def _clean_word(word):
    cleaned = word.lower()
    for char in "-_&+/":
        cleaned = cleaned.replace(char, "")
    return cleaned.strip()


class Lang:
    Words = {}

    def add(self, w):
        key = _clean_word(w)
        if key != '':
            if key not in self.Words:
                self.Words[key] = w.strip()

    def as_valid_word(self, ss):
        key = _clean_word(ss)
        if key in self.Words:
            return self.Words[key]
        return None


def load_language(path):
    lang = Lang()
    with open(path) as handle:
        lines = handle.readlines()
        for word in lines:
            lang.add(word)
    if len(lang.Words) == 0:
        print('ERROR: no loaded words')
    return lang


def index_removed_from_string(index, string):
    return string[0 : index : ] + string[index + 1 : :]


def all_permutations(string):
    if len(string) <= 1:
        yield string
    else:
        for index, char in enumerate(string):
            rest_of_string = index_removed_from_string(index, string)
            for permutation in all_permutations(rest_of_string):
                yield char + permutation


def main():
    parser = argparse.ArgumentParser(description="print anagrams")
    parser.add_argument('dictionary', metavar='d', help='the dictionary to use')
    parser.add_argument('word', metavar='w', help='the word to anagram')
    args = parser.parse_args()

    if args.dictionary == 'ls':
        for permutation in all_permutations(args.word):
            print(permutation)
    else:
        lang = load_language(args.dictionary)
        permutations = set(all_permutations(args.word))

        for permutation in permutations:
            word = lang.as_valid_word(permutation)
            if word is not None:
                print(word)

if __name__ == "__main__":
    main()
