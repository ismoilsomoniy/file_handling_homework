f=open("/home/ismoil/task/data/9.txt","r")
str=f.read()
def main(data:str):
    l=[]
    for i in str:
        if i.isdigit():
            l.append(i)
    return min(l)
print(main(str))
"""
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """