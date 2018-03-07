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
    
    Returns a tuple with multiple dollar amounts.
                (gross, net, fed_dollars, state_dollars, penalty_dollars)

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

    GrossNet = namedtuple('GrossNet', 'gross net fed_dollars state_dollars penalty_dollars')

    # convert to decimal represenation of the percentage
    fed = fed / 100
    state = state / 100
    penalty = penalty / 100

    gross = dollars / (1 - (fed + state + penalty))
    net = dollars - (dollars * fed) - (dollars * state) - (dollars * penalty)

    # Decimal(22.824638).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN)
    # TODO: label the tax dollar amounts better,
    #       because it will depend on if the input was gross or net
    #       so I'll have two sets of dollar amounts in the output.
##    return GrossNet(gross.quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
##                    net.quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
##                    Decimal(gross * fed).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
##                    Decimal(gross * state).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
##                    Decimal(gross * penalty).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
##                    )
    return GrossNet(gross.quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
                    net.quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN),
                    )



if __name__ == '__main__':
    fed = input('Enter the Federal Withholding rate (e.g. 24 for 24%) ')
    state = input('Enter the State Withholding rate (e.g. 4 for 4%) ')
    penalty = input('Enter the any Penalthy Withholding rate (e.g. 10 for 10%) ')
    dollars = input('Enter the dollar amount to calculate from. (e.g. 5122.66 for $5,122.66) ')

    ans = gross_net_calculator(dollars, fed, state, penalty)

    print('\nTax rates used: Fed={}%, State={}%, Penalty={}%'.format(fed, state, penalty))
    print('\nnet({}) -> gross({})\n\nIf the desired net amount is {} dollars, then gross amount needed is {}'.format(dollars, ans.gross, dollars, ans.gross))
    print('\ngross({}) -> net({})\n\nIf a gross amount of {} dollars is requested, the net amount will be {}'.format(dollars, ans.net, dollars, ans.net))
    print('ans={}'.format(ans))
    input('Press <ENTER> to quit.')

