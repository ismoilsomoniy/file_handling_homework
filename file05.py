f=open("/home/ismoil/task/data/5.txt","r")
str=f.read()
def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
"""
    a=0
    dig=0
    for i in str:
        if i.isdigit():
            dig+=1
        else:
            a+=1
    return [dig,a]
print(main(str))
