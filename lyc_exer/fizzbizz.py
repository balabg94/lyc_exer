import doctest
import unittest
import string

def fizzbizz(n):
    """Takes an integer as input which acts as a range and returns fizz for the numbers in that range which are divisible by 3, bizz for numbers in that range divisible by 5, fizzbizz for the numbers in that range divisible by both 3 and 5 and the number itself for those which are diviible by neither 3 or 5.

<-----BEGIN EXAMPLE---->


>>> fizzbizz(20)
'1 2 fizz 4 bizz fizz 7 8 fizz bizz 11 fizz 13 14 fizz 16 17 fizz 19 bizz'
>>> fizzbizz(10)
'1 2 fizz 4 bizz fizz 7 8 fizz bizz'


<-----END EXAMPLE------>

    """
    out = []
    
    for i in range( 1, n+1):
        
        if i == 1 or i == 2:
            out.append(str(i))

        elif i%3 == 0:
            out.append('fizz')

        elif i%5 == 0:
            out.append('bizz')

        elif i%3==0 and i%5==0:
            out.append('fizzbizz')

        else:
            out.append(str(i))
            
    return ' '.join(out)

def abbreviate(s):
    """Takes a string and returns the abbreviation of the same by concatenating the uppercase letter.

<-----BEGIN EXAMPLE---->


>>> abbreviate('Indian Institue of Technology')
'IIT'
>>> abbreviate('Toch Institue of Science and Technology')
'TIST'


<-----END EXAMPLE------>

    """
    out = []
    s = s.split(' ')
    for i in s:
        if i[0].isupper():
            out.append(i[0])
    return ''.join(out)


def panagram(s):
    """ A panagram is a string which has all the alphabets in it. The most famous one being "The quick brown fox jumps over the lazy dog". This fuction takes a string and return True if it is a panagram and False if it is not.

<-----BEGIN EXAMPLE---->

>>> panagram('The quick brown fox jumps over the lazy dog')
True
>>> panagram('Two driven jocks help fax my big quiz.​')
True

<-----END EXAMPLE------>
    """
    s = s.lower()
    for i in string.ascii_lowercase:
        if i not in s:
            return False

        
        if i in s:
            continue
        else:
            return False
    return True

def palindrome(s):
    """ Takes a string as input and returns True if it is a palindrome or returns False if it is not.

<-----BEGIN EXAMPLE---->

>>> palindrome('malayalam')
True
>>> palindrome('civic')
True
>>> palindrome('level')
True

<-----END EXAMPLE------>

    """
    s = s.lower()
    rev = s[::-1]
    if rev == s:
        return True
    else:
        return False


def freq(s):
     """Takes a string as input and returns a dictionary containing the characters in the string and the number of times it's repeated.

<-----BEGIN EXAMPLE---->

>>> freq("the quick brown fox jumps over the lazy dog")
{'t': 2, 'h': 2, 'e': 3, ' ': 8, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r': 2, 'o': 4, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1, 's': 1, 'v': 1, 'l': 1, 'a': 1, 'z': 1, 'y': 1, 'd': 1, 'g': 1}
>>> freq("Malayalam")
{'m': 2, 'a': 4, 'l': 2, 'y': 1}

<-----END EXAMPLE------>

     """

     s = list(s.lower())
     out = {}
     length = len(s)
     for i in range(length):
         count = 0
         alpha = s[i]
         if alpha in out:
             continue
         else:
             for x in range(length):
                 if alpha  == s[x]:
                     count += 1
                 else:
                     continue
             out[alpha] = count
     return out



if __name__ == "__main__":
    doctest.testmod()
