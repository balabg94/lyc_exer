def panagram(s):
    import string
    s = s.lower()
    for i in string.ascii_lowercase:
        if i in s:
            continue
        else:
            return False
    return True
