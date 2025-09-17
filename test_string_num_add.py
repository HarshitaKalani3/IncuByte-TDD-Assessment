import unittest
from string_num_add import add
class SumCalcTestCase(unittest.TestCase):
    def test_empty_str(self):
        res = add("")
        self.assertEqual(res,0)
    def test_one_no(self):
        res = add("1")
        self.assertEqual(res,1)
    def test_two_nos(self):
        res = add("1,5")
        self.assertEqual(res,6)
    def test_multiple_nos(self):
        res = add("3,6,9")
        self.assertEqual(res,18)
    def test_newline_nos(self):
        res = add("1\n2,3")
        self.assertEqual(res,6)
    def test_other_delimiter(self):
        res = add("//;\n1;2")
        self.assertEqual(res,3)
    def test_neg_no(self):
        res = None
        try:
            res = add("1,-1,-2,3")
        except Exception as e:
            res = str(e)
        self.assertEqual(res,"negative numbers not allowed -1,-2")
if __name__=='__main__':
    unittest.main()