def reduce_file_path(path):
    path = path.split('/')
    new = []
    for element in path:
        if element == '..':
            if new:
                new.pop()
        elif element != '.' and element != '/':
            new.append(element)
    new = list(filter(None, new))
    path = '/' + '/'.join(new)
    return path

print(reduce_file_path("/srv/./././././"))
