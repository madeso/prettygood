#!/usr/bin/env python3
import argparse


def _clean_word(w):
    l = w.lower()
    for c in "-_&+/":
        l = l.replace(c, "")
    return l.strip()


class Lang:
    Words = {}

    def add(self, w):
        t = _clean_word(w)
        if t != '':
            if t not in self.Words:
                self.Words[t] = w.strip()

    def as_valid_word(self, ss):
        s = _clean_word(ss)
        if s in self.Words:
            return self.Words[s]
        else:
            return None


def load_language(path):
    lang = Lang()
    with open(path) as f:
        lines = f.readlines()
        for word in lines:
            lang.add(word)
    if len(lang.Words) == 0:
        print('ERROR: no loaded words')
    return lang


def index_removed_from_string(index, string):
    return string[0 : index : ] + string[index + 1 : :]


def all_permutations(p):
    if len(p) <= 1:
        yield p
    else:
        for i, a in enumerate(p):
            b = index_removed_from_string(i, p)
            for s in all_permutations(b):
                r = a + s
                yield r


def main():
    parser = argparse.ArgumentParser(description="print anagrams")
    parser.add_argument('dictionary', metavar='d', help='the dictionary to use')
    parser.add_argument('word', metavar='w', help='the word to anagram')
    args = parser.parse_args()

    if args.dictionary == 'ls':
        for c in all_permutations(args.word):
            print(c)
    else:
        lang = load_language(args.dictionary)
        permutations = set(all_permutations(args.word))

        for s in permutations:
            word = lang.as_valid_word(s)
            if word is not None:
                print(s)

if __name__ == "__main__":
    main()
