import re
def fun(s):
    a = re.match(r'^[a-z][\w-]*@[a-z0-9]+\.[a-z]{1,3}$', s, re.I)
    return (a)