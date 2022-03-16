import glob

def cleanFile(filename):
    #relative file path -> the path from your file to another file
    with open(f"data/{filename}","r",encoding="utf8") as f:
        file = f.readlines()
        
    reducedFile=[]
    for line in file:
        if line != "\n":
            reducedFile.append(line)
    print(reducedFile)
    
    with open(f"out/{filename}","w+",encoding="utf8") as f:
        for line in reducedFile:
            f.write(line)
    print("reduced length of file: ",len(reducedFile))  
            
            
            
books = (glob.glob("data/*.txt"))
bookList=[]
for b in books:
    bookList.append(b[5:])
print(bookList)
for book in bookList:
    cleanFile(book)