def reverse_list(list):
        newlist = []
        for i in reversed(list):
            newlist.append(i)
        return newlist
print reverse_list([1,2,3,4])