mylist = [["a", 33], ["b", 55], ["c", 22]]


def choose_sort_key(element):
    return element[1]


mylist.sort(key=choose_sort_key, reverse=True)
# mylist.sort(key=lambda element: element[1], reverse=True)
print(mylist)
