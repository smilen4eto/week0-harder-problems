def unique_words_count(arr):
    mydict = {}
    for i in range(0, len(arr)):
        mydict[arr[i]] = 1
    return len(mydict)

print(unique_words_count(["HELLO!"] * 10))
