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
        if t == '':
            if t not in self.Words:
                self.Words[t] = w

    def DetermineValidWords(self, l):
        for ss in l:
            s = _clean_word(ss)
            if s in self.Words:
                yield self.Words[s]


def load_language(path):
    lang = Lang()
    with open(path) as f:
        lines = f.readlines()
        for word in lines:
            lang.add(word)
    return lang


def index_removed_from_string(index, strObj):
    return strObj[0 : index : ] + strObj[index + 1 : :]


def ListCombinations(p):
    if len(p) <= 1:
        yield p
    else:
        for i, a in enumerate(p):
            b = index_removed_from_string(i, p)
            for s in ListCombinations(b):
                r = a + s
                yield r


def print_words(lang, input):
    for s in lang.DetermineValidWords(ListCombinations(input)):
        print(s)


def main():
    parser = argparse.ArgumentParser(description="print anagrams")
    parser.add_argument('dictionary', metavar='d', help='the dictionary to use')
    parser.add_argument('word', metavar='w', help='the word to anagram')
    args = parser.parse_args()

    if args.dictionary == 'ls':
        for c in ListCombinations(args.word):
            print(c)
    else:
        lang = load_language(args.dictionary)
        print_words(lang, args.word)

if __name__ == "__main__":
    main()
