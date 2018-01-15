import unittest
from decimal import *
from gross_net_calculator import gross_net_calculator

class Test_gross_net_calculator_test1(unittest.TestCase):
    getcontext().prec = 6
    known_answers_gross_net_calculator = [
        ((5555.56, 24, 4, 0), (Decimal(7716.06).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN), Decimal(4000).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN)))
        ]
    
    def test_gross_net_calculator_known_answers(self):
        for case, ans in self.known_answers_gross_net_calculator:
            test_ans = gross_net_calculator(dollars=case[0], fed=case[1], state=case[2], penalty=case[3])
            print('test_ans={}\nans={}'.format(test_ans, ans))
            self.assertEqual(test_ans, ans)

    def test_A(self):
        self.fail("Not implemented")

if __name__ == '__main__':
    unittest.main()
