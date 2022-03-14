import os, re
'''
    For the given path, get the List of all files in the directory tree
    and replace occurences in these files

    WARNING: not for production use!
'''
def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles

def filterFiles(fileList, extension):
    filtered = list()
    extLen = len(extension)
    
    for file in fileList:
        if file[-extLen:] == extension:
            filtered.append(file)

    return filtered

def replaceInFile(fileIn, stringOld, stringNew):
    with open(fileIn, "rt", encoding="utf-8") as file:
        x = file.read()
	
    with open(fileIn, "wt", encoding="utf-8") as file:
        x = x.replace(stringOld,stringNew)
        file.write(x)
    
def main():
    
    dirName = './';
    
    # Get the list of all files in directory tree at given path
    listOfFiles = getListOfFiles(dirName)
    
    # Get the list of all files in directory tree at given path
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
        
    filteredList = filterFiles(listOfFiles, '.html')
    
    # Replace all vwo ones    
    for elem in filteredList:
        replaceInFile(elem, 'https://havovwo.nl/vwo/omzet', './bestanden')
        
    # Replace all havo ones
    for elem in filteredList:
        replaceInFile(elem, 'https://havovwo.nl/havo/omzet', './bestanden')        
        
        
if __name__ == '__main__':
    main()
