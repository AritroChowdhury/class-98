def countWordsFromFile():
    fileName=input('Enter The File Name-')
    file=open(fileName,'r')
    noOfWords=0
    for line in file:
        word=line.split()
        noOfWords=noOfWords+len(word)
    print('No Of Words' )
    print(noOfWords)

countWordsFromFile()    