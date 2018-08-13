def abbreviate(s):
    out = []
    for i in s:
        if i.isupper():
            out.append(i)
        else:
            continue
    return ''.join(out)
