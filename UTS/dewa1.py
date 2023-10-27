import unittest

class TestCaseString(unittest.TestCase):

#test case string 'dewa' diubah menjadi kapital apakah sama dengan 'DEWA'
  #jika hasil success
    def test_uppersucc(self):
        self.assertEqual('dewa'.upper(), 'DEWA')
  #jika hasil fail
    def test_upperfail(self):
        self.assertEqual('dewa'.upper(), 'Dewa')

#test case string input merupakan kapital semua
    def test_isupper(self):
        self.assertTrue('DEWA'.isupper())
        self.assertFalse('Dewa'.isupper())

#test case jika string input di split, apakah sesuai dengan hasil yang ditentukan
    def test_split(self):
        s = 'Dewa Irtzadhany'
        self.assertEqual(s.split(), ['Dewa', 'Irtzadhany'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
