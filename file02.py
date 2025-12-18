f=open("/home/ismoil/task/data/2.txt","r")
str=f.read()
def main(data:str):
    return len(str)
print(main(str))
"""
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
"""