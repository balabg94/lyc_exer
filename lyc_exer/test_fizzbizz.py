import fizzbizz
import unittest


class Testfizzbizz(unittest.TestCase):
    def test_panagram(self):
        input = 'The quick brown fox jumps over the lazy dog.'
        expected_out = True
        actual_out  = fizzbizz.panagram(input)
        self.assertEqual(expected_out, actual_out)
        
    def test_palidrome(self):
        input = 'Malayalam'
        expected_out = True
        actual_out  = fizzbizz.palindrome(input)
        self.assertEqual(expected_out, actual_out)
        
    def test_fizzbizz(self):
        input = 10
        expected_out = '1 2 fizz 4 bizz fizz 7 8 fizz bizz'
        actual_out  = fizzbizz.fizzbizz(input)
        self.assertEqual(expected_out, actual_out)

    def test_abbreviate(self):
        input = 'Toch Institute of Science and Technology'
        expected_out = 'TIST'
        actual_out  = fizzbizz.abbreviate(input)
        self.assertEqual(expected_out, actual_out)

    def test_panagram(self):
        input = 'The quick brown fox jumps over the lazy dog'
        expected_out = {
            't': 2,
            'h': 2,
            'e': 3,
            ' ': 8,
            'q': 1,
            'u': 2,
            'i': 1,
            'c': 1,
            'k': 1,
            'b': 1,
            'r': 2,
            'o': 4,
            'w': 1,
            'n': 1,
            'f': 1,
            'x': 1,
            'j': 1,
            'm': 1,
            'p': 1,
            's': 1,
            'v': 1,
            'l': 1,
            'a': 1,
            'z': 1,
            'y': 1,
            'd': 1,
            'g': 1}
        actual_out  = fizzbizz.freq(input)
        self.assertEqual(expected_out, actual_out)


        
if __name__ == '__main__':
    unittest.main()
