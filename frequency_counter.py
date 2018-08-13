def freq(s):
    s = list(s.lower())
    out = {}
    length = len(s)
    for i in range(length):
        count = 0
        #print(i)
        alpha = s[i]
        if alpha in out:
           # print("looping")
            continue
        else:
            for x in range(length):
             #   print(x)
              #  print(s[i])
               # print(s[x])
                if alpha  == s[x]:
                    count += 1
                #    print(f"{count} {s[i]}")
                else:
                 #   print("next")
                    continue
            out[alpha] = count
    return out
