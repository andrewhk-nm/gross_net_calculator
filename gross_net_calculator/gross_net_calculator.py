""" Given particular tax withholding rates and a dollar amount,
    return the gross or net amount.
"""
# TDD
# Use tkinter
# TODO use integers instead of Decimals, apparently.
# TODO: Maybe make different functions to return the dollar amounts
#       that are getting withheld.
from decimal import *
from collections import namedtuple

def gross_net_calculator(dollars, fed=0, state=0, penalty=0):
    """ Takes a dollar amount, dollars, and the fed, state and penalty tax rates
    as decimals.
    e.g. dollars=5000 is $5000.00
         fed=24 is 24%
         state=2.3 is 2.3%
    
    Returns tuples with multiple dollar amounts, as well as display text for pretty
        printing.
            The first one assumes the input dollars is a Net amount.
            The second assumes the input dollars is a Gross amount. 
               ((gross_dollars, fed_dollars, state_dollars, penalty_dollars, printable_summary),
                (net_dollars, fed_dollars, state_dollars, penalty_dollars, printable_summary)
               ) 

                

    gross is the answer if dollars is the "net" amount desired given the tax
    rates.
    net is the answer if dollars is the "gross" amount.
    """

    # Create the variables of the Decimal type to avoid
    # float rounding issues
    getcontext().prec = 28
    dollars = Decimal(dollars)
    fed = Decimal(fed)
    state = Decimal(state)
    penalty = Decimal(penalty)

    # These are the named tuples for the output
    Gn_shell_type = namedtuple('Gross_Net_Shell', 'input_was_gross input_was_net')
    Gn_output_type = namedtuple('Gross_Net_Output', 'output_dollars federal state fed_penalty summary')

    # convert to decimal represenation of the percentage
    fed = fed / 100
    state = state / 100
    penalty = penalty / 100

    gross = dollars / (1 - (fed + state + penalty))
    net = dollars - (dollars * fed) - (dollars * state) - (dollars * penalty)

    # create a named tuple in the custom output format that will show all related info
    # when assuming the input dollars is the gross amount
    input_was_gross = Gn_output_type(Decimal(net).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
                                     Decimal(dollars * fed).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
                                     Decimal(dollars * state).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
                                     Decimal(dollars * penalty).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
                                     '''Assuming the input dollar value (${dollars:.2f}) is the Gross amount,
the Net amount is ${net:.2f},
{fed_pct:.2f}% withheld for Federal taxes is ${fed_dollars:.2f},
{state_pct:.2f}% withheld for State taxes is ${state_dollars:.2f},
and a {penalty_pct:.2f}% Federal Penalty tax is ${penalty_dollars:.2f}.'''.format(dollars=dollars,
                                                                                  net=net,
                                                                                  fed_pct=fed * 100,
                                                                                  fed_dollars=dollars * fed,
                                                                                  state_pct=state * 100,
                                                                                  state_dollars=dollars * state,
                                                                                  penalty_pct=penalty * 100,
                                                                                  penalty_dollars=dollars * penalty,
                                                                                 ),
                                    )
    # create a named tuple in the custom output format that will show all related info
    # when assuming the input dollars is the net amount
    input_was_net = Gn_output_type(Decimal(gross).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
                                   Decimal(gross * fed).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
                                   Decimal(gross * state).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
                                   Decimal(gross * penalty).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
                                   '''Assuming the input dollar value (${dollars:.2f}) is the Net amount,
the Gross amount is ${gross:.2f},
{fed_pct:.2f}% withheld for Federal taxes is ${fed_dollars:.2f},
{state_pct:.2f}% withheld for State taxes is ${state_dollars:.2f},
and a {penalty_pct:.2f}% Federal Penalty tax is ${penalty_dollars:.2f}.'''.format(dollars=dollars,
                                                                                  gross=gross,
                                                                                  fed_pct=fed * 100,
                                                                                  fed_dollars=gross * fed,
                                                                                  state_pct=state * 100,
                                                                                  state_dollars=gross * state,
                                                                                  penalty_pct=penalty * 100,
                                                                                  penalty_dollars=gross * penalty,
                                                                                 ),
                                  )
    shell = Gn_shell_type(input_was_gross, input_was_net)

    # Print the summaries
    print('\n')
    print(shell.input_was_gross.summary)
    print('\n')
    print(shell.input_was_net.summary)
    print('\n')
    
    return shell

##    return GrossNet(gross.quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
##                    net.quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
##                    Decimal(gross * fed).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
##                    Decimal(gross * state).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
##                    Decimal(gross * penalty).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
##                    )
##    return GrossNet(gross.quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
##                    net.quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
##                    )



if __name__ == '__main__':
    fed = input('Enter the Federal Withholding rate (e.g. 24 for 24%) ')
    state = input('Enter the State Withholding rate (e.g. 4 for 4%) ')
    penalty = input('Enter the any Penalthy Withholding rate (e.g. 10 for 10%) ')
    dollars = input('Enter the dollar amount to calculate from. (e.g. 5122.66 for $5,122.66) ')

    ans = gross_net_calculator(dollars, fed, state, penalty)

    print(ans.input_was_gross.summary)

##
##    print('\nTax rates used: Fed={}%, State={}%, Penalty={}%'.format(fed, state, penalty))
##    print('\nnet({}) -> gross({})\n\nIf the desired net amount is {} dollars, then gross amount needed is {}'.format(dollars, ans.gross, dollars, ans.gross))
##    print('\ngross({}) -> net({})\n\nIf a gross amount of {} dollars is requested, the net amount will be {}'.format(dollars, ans.net, dollars, ans.net))
##    print('ans={}'.format(ans))
    input('Press <ENTER> to quit.')

