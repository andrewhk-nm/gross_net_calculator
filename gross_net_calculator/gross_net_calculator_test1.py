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
        Gn_output_type = namedtuple('Gross_Net_Output', 'output_dollars federal state fed_penalty summary')

        # input_value is what is passed to the function
        #             dollars, fed, state, fed_penalty
        # gross is the 
        input_value = (5555.56, 24, 4, 0)
        input_was_gross = Gn_output_type(Decimal(4000).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
                                         Decimal(1333.33).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
                                         Decimal(222.22).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
                                         Decimal(0).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
                                         '''Assuming the input dollar value (${dollars:.2f}) is the Gross amount,
the Net amount is ${net:.2f},
{fed_pct:.2f}% withheld for Federal taxes is ${fed_dollars:.2f},
{state_pct:.2f}% withheld for State taxes is ${state_dollars:.2f},
and a {penalty_pct:.2f}% Federal Penalty tax is ${penalty_dollars:.2f}.'''.format(dollars=5555.56,
                                                                                  net=4000,
                                                                                  fed_pct=24.00,
                                                                                  fed_dollars=1333.33,
                                                                                  state_pct=4.00,
                                                                                  state_dollars=222.22,
                                                                                  penalty_pct=0.00,
                                                                                  penalty_dollars=0.00,
                                                                                 ),
                                        )
        input_was_net = Gn_output_type(Decimal(7716.06).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
                                       Decimal(1851.8544).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
                                       Decimal(308.64).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
                                       Decimal(0).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
                                       '''Assuming the input dollar value (${dollars:.2f}) is the Net amount,
the Gross amount is ${gross:.2f},
{fed_pct:.2f}% withheld for Federal taxes is ${fed_dollars:.2f},
{state_pct:.2f}% withheld for State taxes is ${state_dollars:.2f},
and a {penalty_pct:.2f}% Federal Penalty tax is ${penalty_dollars:.2f}.'''.format(dollars=5555.56,
                                                                                  gross=7716.06,
                                                                                  fed_pct=24.00,
                                                                                  fed_dollars=1851.85,
                                                                                  state_pct=4.00,
                                                                                  state_dollars=308.64,
                                                                                  penalty_pct=0.00,
                                                                                  penalty_dollars=0.00,
                                                                                 ),
                                      )
        shell = Gn_shell_type(input_was_gross, input_was_net)

        self.assertEqual(gross_net_calculator(*input_value), shell)
        
         
    
    def test_gross_net_calculator_known_answers(self):
        """ Test a sample of known answers
        """

        # specificially test the output format of the answer.
        Gn_shell_type = namedtuple('Gross_Net_Shell', 'input_was_gross input_was_net')
        Gn_output_type = namedtuple('Gross_Net_Output', 'output_dollars federal state fed_penalty summary')
        
        def dec(value):
            """ Takes an answer value and outputs a Decimal type with the standard options.
                Helps cut down on the repetitive text in the known_answers_ variable
            """
            return Decimal(value).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN)

        summary_template_grs = '''Assuming the input dollar value (${dollars:.2f}) is the Gross amount,
the Net amount is ${net:.2f},
{fed_pct:.2f}% withheld for Federal taxes is ${fed_dollars:.2f},
{state_pct:.2f}% withheld for State taxes is ${state_dollars:.2f},
and a {penalty_pct:.2f}% Federal Penalty tax is ${penalty_dollars:.2f}.'''
        
        summary_template_net = '''Assuming the input dollar value (${dollars:.2f}) is the Net amount,
the Gross amount is ${gross:.2f},
{fed_pct:.2f}% withheld for Federal taxes is ${fed_dollars:.2f},
{state_pct:.2f}% withheld for State taxes is ${state_dollars:.2f},
and a {penalty_pct:.2f}% Federal Penalty tax is ${penalty_dollars:.2f}.'''

        gross_net_calculator.__subclasshook__

        known_inputs = [(5555.56, 24, 4, 0),
                       ]

        known_outputs = [(Gn_output_type(dec(4000),
                                         dec(1333.33),
                                         dec(222.22),
                                         dec(0),
                                         summary_template_net.format(dollars=5555.56,
                                                                     gross=7716.06,
                                                                     fed_pct=24.00,
                                                                     fed_dollars=1851.85,
                                                                     state_pct=4.00,
                                                                     state_dollars=308.64,
                                                                     penalty_pct=0.00,
                                                                     penalty_dollars=0.00,)
                                        ),
                          Gn_output_type(dec(7716.06),
                                         dec(1851.85),
                                         dec(308.64),
                                         dec(0),
                                         summary_template_grs.format(dollars=5555.56,
                                                                     net=4000,
                                                                     fed_pct=24.00,
                                                                     fed_dollars=1333.33,
                                                                     state_pct=4.00,
                                                                     state_dollars=222.22,
                                                                     penalty_pct=0.00,
                                                                     penalty_dollars=0.00,)
                                        )
                                       ),
                        ]

        # Create a zip iterable, matching the inputs to the outputs.
        known_answers_gross_net_calculator = zip(known_inputs, known_outputs)
        
        for case, known_ans in known_answers_gross_net_calculator:
            known_ans = Gn_shell_type(*known_ans)
            test_ans = gross_net_calculator(dollars=case[0], fed=case[1], state=case[2], penalty=case[3])
            print('test_ans=\n{}\n\nknown_ans=\n{}\n'.format(test_ans, known_ans))
            self.assertEqual(test_ans, known_ans)

if __name__ == '__main__':
    unittest.main()
