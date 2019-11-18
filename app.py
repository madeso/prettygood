class NotInitialized(Exception):
    pass
    
class App(object):
    _Company = ""
    _ReadableAppName = ""
    _Code = ""
    _init = False
    
    def __init__(self, company="", readableAppName="", appCode="", init=True):
        self._Company = company
        self._ReadableAppName = readableAppName
        self._Code = appCode
        self._init = init
    
    @property
    def Company(self):
        if self._init == False:
            raise NotInitialized()
        return self._Company
    
    @property
    def ReadableAppName(self):
        if self._init == False:
            raise NotInitialized()
        return self._ReadableAppName
    
    @property
    def Code(self):
        if self._init == False:
            raise NotInitialized()
        return self._Code

instance = App(init=False)

if __name__ == "__main__":
    instance = App("Acme Corp.", "App 2.0", "acmecorp")
    print instance.Code
    print instance.Company
    print instance.ReadableAppName