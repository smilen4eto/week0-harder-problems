def count_words(arr):
    mydict = {}
    for i in range(0, len(arr)):
        mydict[arr[i]] = arr.count(arr[i])
    return mydict

print(count_words(["apple", "banana", "apple", "pie"]))
