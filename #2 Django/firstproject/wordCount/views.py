from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def result(request):
    sentence = request.GET['sentence']
    wordList = sentence.split()
    wordDict = {}
    
    for word in wordList:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1
    
    return render(request, "result.html", {'fulltext' : sentence, 'count' : len(wordList), "wordDict" : wordDict.items})