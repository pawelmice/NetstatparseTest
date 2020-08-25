import subprocess

class NetstatStdoutParser(object):

    def __init__(self):
        self.dat = []
        self.table = []
        self.temp = []

    def loadFile(self, filepath):
        f = open(filepath, "r")
        d = f.readlines()
        f.close()
        self.dat = d
    
    def runCommand(self):
        proc = subprocess.run(["netstat", "-o"], capture_output=True, text=True)
        self.dat = proc.stdout

    def parseFile(self):
        word = ""
        wordlist = []
        for l in self.dat:
            for z in l:
                if z != " " and z != "\n":
                    word += z
                else:
                    if word.__len__() > 0:
                        wordlist.append(word)
                    word = ""
            if wordlist.__len__() >0:
                self.table.append(wordlist)
            wordlist = []

    def parseCMD(self):
        word = ""
        for l in self.dat:
            if l != " " and l != "\n":
                word +=l
            else:
                if word.__len__() > 0:
                    if self.temp.__len__() < 4:
                        self.temp.append(word) 
                    else:
                        self.table.append(self.temp)
                        self.temp = []
                    word =""
                
    def display(self):
        for l in self.table:
            print(l)

test = NetstatStdoutParser()
test.loadFile("out.txt")
test.parseFile()
# test.runCommand()
# test.parseCMD()
test.display()