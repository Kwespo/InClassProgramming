import unittest

from tests.area import Area



class TestArea(unittest.TestCase):

  def test_int(self):
    result = Area(3,5) #return 25
    self.assertEqual(result, 15) #if the result is not 20 it will fail.

  def test_Float1(self):
    result = Area(2.3,7.87) #return 25
    self.assertEqual(result, 18.101) #if the result is not 20 it will fail.

  def test_Float2(self):
    result = Area(2.3,7.8) #return 25
    self.assertEqual(result, 17.94) #if the result is not 20 it will fail.

  def test_Text(self):
    result = Area('a', 'b')
    self.assertEqual(result, "Cannot convert given values into a 'float'")

  def test_NegNum(self):
    result = (Area(-1, 10))
    self.assertEqual(result, 10)

  def test_DivByZero(self):
    result = Area(5, 0)
    self.assertEqual(result,  0)

if __name__ == '__main__':
  unittest.main()