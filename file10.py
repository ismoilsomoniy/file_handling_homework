f=open("/home/ismoil/task/data/10.txt","r")
str=f.read()
def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
"""
    s=str.split("\n")
    l=[]
    for i in s:
        l.append(len(i))
    return max(l)
print(main(str))
