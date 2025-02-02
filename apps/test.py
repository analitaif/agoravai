import unittest
from apps.validators import Validators

class Testando(unittest.TestCase):


   def test_string(self):
       resultado_1 = Validators.check_valid_identifier(self, "abc")
       self.assertTrue(resultado_1)


       resultado_2 = Validators.check_valid_identifier(self, "_Abc")
       self.assertTrue(resultado_2)


       resultado_3 = Validators.check_valid_identifier(self, "1425")
       self.assertFalse(resultado_3)


       resultado_4 = Validators.check_valid_identifier(self, "@def")
       self.assertFalse(resultado_4)




if __name__ == "__main__":
   unittest.main()
