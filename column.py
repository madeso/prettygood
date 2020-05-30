#!/usr/bin/env python3

import pattern

class Column:
    def __init__(self, name, pat):
        self.title = name
        self.display_pattern = pattern.Compile(pat or name)
        self.optional_sort_pattern = None

    def sort_pattern(self):
        if self.optional_sort_pattern == None:
            return self.display_pattern
        else:
            return self.optional_sort_pattern

    def get_display(self, functions, data):
        return self.display_pattern.eval(functions, data)

    def get_sort(self, functions, data):
        return self.sort_pattern().eval(functions, data)
