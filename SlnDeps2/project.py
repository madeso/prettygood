from enum import Enum
import os.path
import xml.etree.ElementTree as ET


class Build(Enum):
        Unknown = 1
        Application = 2
        Static = 3
        Shared = 4


class Project:
    """
    :type Solution: Solution
    :type DisplayName: string
    :type Path: string
    :type Id: string
    :type Type: Build
    :type deps: list[Project]
    :type sdeps: list[string]
    """
    Solution = None
    DisplayName = ""
    Path = ""
    Id = ""
    Type = Build.Unknown
    deps = []
    sdeps = []

    def __init__(self, Solution, Name, Path, Id):
        """
        :type Solution: Solution
        :type Name: string
        :type Path: string
        :type Id: string
        """
        self.Solution = Solution
        self.Name = Name
        self.Path = Path
        self.Id = Id

    @property
    def Name(self):
        """
        @retype: string
        """
        return self.DisplayName.replace('-', '_')

    @Name.setter
    def Name(self, value):
        """
        :param value: string
        """
        self.DisplayName = value

    def __str__(self):
        return self.Name

    def resolve(self, projects):
        """
        :param projects: dict[string, Project]
        """
        for s in self.sdeps:
            self.deps.append(projects[s])

    def loadInformation(self):
        p = Gen(self.Path)
        if not os.path.isfile(p):
            return
        doc = ET.parse(p)
        l = []
        """:type : list[string]"""
        for n in doc.getroot().findall("VisualStudioProject/Configurations/Configuration[@ConfigurationType]"):
            v = n.attrib["ConfigurationType"]
            if v in l is False:
                l.append(v)
        self.Type = Build.Unknown

        if len(l) != 0:
            suggestedType = l[0]
            if suggestedType == "2":
                self.Type = Build.Shared
            elif suggestedType == "4":
                self.Type = Build.Static
            elif suggestedType == "1":
                self.Type = Build.Application

def Gen(pa):
    """
    :param pa: string
    :return: string
    """
    p = pa
    if os.path.isfile(p):
        return p
    p = pa + ".vcxproj"
    if os.path.isfile(p):
        return p
    return ""