f=open("/home/ismoil/task/data/6.txt","r")
str=f.read()
def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    l=[]
    s=str.split()
    for i in range(len(s)):
        l.append(len(s[i]))
    return l
print(main(str))
