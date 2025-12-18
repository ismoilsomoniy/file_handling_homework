f=open("/home/ismoil/task/data/4.txt","r")
str=f.read()
l=[]
def main(data:str):
    for i in str:
        if not i.isdigit():
            l.append(i)
    return l
print(main(str))
"""
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
"""