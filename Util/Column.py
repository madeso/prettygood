class Column(object):
    def __init__(self, name):
        self.title = name
        self.displayPattern = Pattern("eval " + name)
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
        if header != None:
            header.Text = title
    

    @property
    def Display(self):
        return self.displayPattern

    @property
    def Sort(self):
        if self.sortPattern == None:
            return self.displayPattern
        else:
            return self.sortPattern