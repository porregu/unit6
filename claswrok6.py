
def remove_duplicates(paper):
    guffy=[]
    for x in paper:
        if x not in guffy:
            guffy.append(x)
    return guffy
print(remove_duplicates([1,2,3,2,1,2,3,4,3,2,2,3,4,4,3,2,1,2,3,4]))