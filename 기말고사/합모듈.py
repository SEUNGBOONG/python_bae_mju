
pi = 3.14
def add(end):
    sum=0
    for i in range(end+1):
        sum += i
    return sum

def gop(end):
    gopsum=1
    for i in range(end):
        gopsum *=i+1
    return gopsum