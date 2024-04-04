import random

def get_quote(path="../Assets/Files/Citations.txt"):
    """from a text file with one quote per line, selects a random line"""
    with open(path, mode="r") as file:
        lines = file.readlines() # List of quotes
        i,j =0, random.randint(0, len(lines))
        for line in lines:
            if i == j :
                return line
            else :
                i+=1
