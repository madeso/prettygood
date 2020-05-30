#!/usr/bin/env python3

import pattern

class Column(object):
    def __init__(self, name):
        self.title = name
        self.displayPattern = pattern.Compile(name)
        self.sortPattern = None
        self.header = None

    @property
    def Header(self):
        return self.header
    
    @Header.setter
    def Header(self, value):
        self.header = value
        self.updateText()
    
    def updateText(self):
        if self.header != None:
            self.header.Text = self.title
    

    @property
    def Display(self):
        return self.displayPattern

    @property
    def Sort(self):
        if self.sortPattern == None:
            return self.displayPattern
        else:
            return self.sortPattern
