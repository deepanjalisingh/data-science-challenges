import re
n=int(input())
for i in range(0,n):
    x=input()
    print(bool(re.match(r"^[+-\.]?[0-9]*\.[0-9]+$",x)))
