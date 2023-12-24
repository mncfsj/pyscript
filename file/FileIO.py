def getFileLines(file):
    fileLines = []
    with open(file) as f:
        fileLines = f.readlines()
    return fileLines

def writeFileLines(file, lines):
    with open(file, "w") as f:
        f.writelines(lines)

def deleteFirstLine(file):
    fileLines = getFileLines(file)
    fileLines = fileLines[1:]
    writeFileLines(file, fileLines)

def appendFileLine(file, line):
    fileLines = getFileLines(file)
    fileLines.append(line)
    writeFileLines(file, fileLines)

def InsertUpLine(file, str, line):
    oldFileLines = getFileLines(file)
    newFileLines = []
    for fileLine in oldFileLines:
        if (str in fileLine):
            newFileLines.append(line)
        newFileLines.append(fileLine)
    writeFileLines(file, newFileLines)

def InsertDownLine(file, str, line):
    oldFileLines = getFileLines(file)
    newFileLines = []
    for fileLine in oldFileLines:
        newFileLines.append(fileLine)
        if (str in fileLine):
            newFileLines.append(line)
    writeFileLines(file, newFileLines)

def copyFile(srcFile, destFile):
    fileLines = getFileLines(srcFile)
    writeFileLines(destFile, fileLines)
