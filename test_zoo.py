import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
    
    #age < 0
    def test_lowerthanzero(self):
        self.assertEqual(self.zoo.get_ticket_price(-1),"error")

    #0 <= age <=12
    def test_b2(self):
        self.assertEqual(self.zoo.get_ticket_price(0),50)

    #13 <= age <= 20
    def test_b3(self):
        self.assertEqual(self.zoo.get_ticket_price(20),100)

    #21 <= age <= 60
    def test_b4(self):
        self.assertEqual(self.zoo.get_ticket_price(21),150)
    
    #Age > 60
    def test_b5(self):
        self.assertEqual(self.zoo.get_ticket_price(75),100)
if __name__ == '__main__':
    unittest.main()