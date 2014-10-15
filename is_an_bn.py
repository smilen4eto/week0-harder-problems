def is_an_bn(word):
    if len(word) % 2 != 0:
        return False
    else:
        l = int(len(word)/2)
        new = "a"*l + "b"*l
        if new == word:
            return True
        else:
            return False

print(is_an_bn("aabb"))
