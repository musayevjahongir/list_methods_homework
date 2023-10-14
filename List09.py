def main(fruits):
    """
    A list called “fruits” is given and is five in length and contains at least one “apple”. Calculate how many “apple” were involved and return the indexes in a list view.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    i=0
    s=[]
    j=0
    while i<len(fruits):
        if fruits[i]=="apple":
            s.append(i)
            j+=1
        i+=1
    s.insert(0,j)
    return s
print(main(["apple", "banana", "apple", "pear", "apple"]))