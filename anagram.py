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
                if isinstance(permutation, list):
                    yield [char] + permutation
                else:
                    yield char + permutation


def main():
    parser = argparse.ArgumentParser(description="print anagrams")
    parser.add_argument('dictionary', metavar='d', help='the dictionary to use')
    parser.add_argument('word', metavar='w', help='the word to anagram')
    args = parser.parse_args()

    if args.dictionary == 'ls':
        for permutation in all_permutations(args.word):
            print(permutation.strip())
    elif args.dictionary == 'lsl':
        for permutation in all_permutations(args.word.split(' ')):
            print(' '.join(permutation))
    else:
        lang = load_language(args.dictionary)
        permutations = set(p.strip() for p in all_permutations(args.word.lower()))

        for permutation in permutations:
            words = [lang.as_valid_word(w) for w in permutation.split(' ')]
            if all(word is not None for word in words):
                print(' '.join(words))

if __name__ == "__main__":
    main()
