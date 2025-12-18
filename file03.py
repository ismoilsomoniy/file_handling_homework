f=open("/home/ismoil/task/data/3.txt","r")
str=f.read()
l=[]
def main(data:str):
    for i in str:
        if i.isdigit():
            l.append(i)
    return l
print(main(str))
"""
    The data is from the file. Return the digits as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """