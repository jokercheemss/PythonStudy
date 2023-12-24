def my(s,t):
    m = len(s)
    n = len(t)
    if m<n:
        return -1
    i = 0
    while i<=m-n:
        j = 0
        while j<n:
            if s[i+j]!=t[j]:
                break
            j+=1
        if j ==n:
            return i
        i+=1
    return -1
s = "ababcabcd12ab"
print(my(s,"abc"),s.find("abc"))
print(my(s,"ad"),s.find("ad"))


def is_symmetrical(str):
    length = len(str)
    for i in range(length / 2):
        if str[i] != str[length - i - 1]:
            return False
    return True


input_pwd = "1233213"
def is_symmetrical(str):
    length = len(str)
    for i in range(length/2):
        if str[i] != str[length-i-1]:
            return False
    return True


def is_symmetrical(str):
    length = len(str)
    for i in range(length / 2):
        if str[i] != str[length - i - 1]:
            return False
    return True
input_pwd = "1233213"
print(is_symmetrical(input_pwd))


