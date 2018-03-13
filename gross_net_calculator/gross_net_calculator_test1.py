import unittest
from decimal import *
from gross_net_calculator import gross_net_calculator
from functools import namedtuple

class Test_gross_net_calculator_test1(unittest.TestCase):
    getcontext().prec = 6

    # General Tuple Form
    # ((input_tuple), ((gross_tuple), (net_tuple)),
    # )

    def test_gross_net_calculator_answer_format(self):
        # specificially test the output format of the answer.
        Gn_shell_type = namedtuple('Gross_Net_Shell', 'input_was_gross input_was_net')
        Gn_output_type = namedtuple('Gross_Net_Output', 'dollars federal state fed_penalty summary')

        # input_value is what is passed to the function
        #             dollars, fed, state, fed_penalty
        # gross is the 
        input_value = (5555.56, 24, 4, 0)
        input_was_gross = Gn_output_type(Decimal(4000).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
                                         Decimal(1333.33).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
                                         Decimal(222.22).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
                                         Decimal(0).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
                                         'Assuming the input dollar value ($5555.56) is the Gross amount,\nthe Net amount is $4000.00,\nthe 24% Federal tax will be $1333.33,\nthe 4% State tax will be $222.22,\nand the 0% Federal Penalty will be $0.',
                                        )
        input_was_net = Gn_output_type(Decimal(7716.06).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
                                       Decimal().quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
                                       Decimal().quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
                                       Decimal(0).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
                                       'Assuming the input dollar value ($5555.56) is the Net amount,\nthe Gross amount is $7716.06,\nthe 24% Federal tax will be $1851.85,\nthe 4% State tax will be $308.64,\nand the 0% Federal Penalty will be $0.',
                                      )
        shell = Gn_shell_type(input_was_gross, input_was_net)

        self.assertEqual(gross_net_calculator(*input_value), shell)
        
         
    
    def test_gross_net_calculator_known_answers(self):
        known_answers_gross_net_calculator = [
                ((5555.56, 24, 4, 0),
                 ((Decimal(7716.06).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN), )),
                  (Decimal(4000).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN), )
                 )
                ]
        for case, ans in known_answers_gross_net_calculator:
            test_ans = gross_net_calculator(dollars=case[0], fed=case[1], state=case[2], penalty=case[3])
            print('test_ans={}\nans={}'.format(test_ans, ans))
            self.assertEqual(test_ans, ans)

if __name__ == '__main__':
    unittest.main()
