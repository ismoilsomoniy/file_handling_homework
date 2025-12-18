f=open("/home/ismoil/task/data/8.txt","r")
str=f.read()
def main(str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
"""
    l=[]
    for i in str:
        if i.isdigit():
            l.append(i)
    return max(l)
print(main(str))
