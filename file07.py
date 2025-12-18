f=open("/home/ismoil/task/data/7.txt","r")
str=f.read()
def main(data:str):
    sum=0
    for i in str:
        if i.isdigit():
            sum+=int(i)
    return sum
print(main(str))
"""
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
"""