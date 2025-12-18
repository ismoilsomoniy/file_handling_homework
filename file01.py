f=open("/home/ismoil/task/data/1.txt","r")
str=f.read()
l=[]
def main(data:str):
    
"""
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
"""
    for i in str:
        if i.isdigit():
            l.append(int(i))
    return l
print(main(str))

