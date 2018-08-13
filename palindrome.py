def palindrome(s):
    s = s.lower()
    rev = []
    for i in range(-1, -len(s)-1, -1):
        rev.append(s[i])
    rev = ''.join(rev)
    if rev == s:
        return True
    else:
        return False
