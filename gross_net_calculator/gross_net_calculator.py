""" Given particular tax withholding rates and a dollar amount,
    return the gross or net amount.
"""
# TDD
from decimal import *
from collections import namedtuple

def gross_net_calculator(dollars, fed, state, penalty):
    """ Takes a dollar amount, dollars, and the fed, state and penalty tax rates as decimals.
    Returns a tuple with two dollar amounts. (gross, net)
    gross is the answer if dollars is the "net" amount desired given the tax rates.
    net is the answer if dollars is the "gross" amount.
    """

    getcontext().prec = 28
    dollars = Decimal(dollars)
    fed = Decimal(fed)
    state = Decimal(state)
    penalty = Decimal(penalty)

    GrossNet = namedtuple('GrossNet', 'gross net')
    
    fed = fed / 100
    state = state / 100
    penalty = penalty / 100

    gross = dollars / (1 - (fed + state + penalty))
    net = dollars - (dollars * fed) - (dollars * state) - (dollars * penalty)

    # Decimal(22.824638).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN)
    r = GrossNet(gross.quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN), net.quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN))
        
    return r



if __name__ == '__main__':
    fed = input('Enter the Federal Withholding rate (e.g. 24 for 24%) ')
    state = input('Enter the State Withholding rate (e.g. 4 for 4%) ')
    penalty = input('Enter the any Penalthy Withholding rate (e.g. 10 for 10%) ')
    dollars = input('Enter the dollar amount to calculate from. (e.g. 5122.66 for $5,122.66) ')

    ans = gross_net_calculator(dollars, fed, state, penalty)

    print('If the desired net amount is {} dollars, then gross amount needed is {}'.format(dollars, ans.gross))
    print('If a gross amount of {} dollars is requested, the net amount will be {}'.format(dollars, ans.net))
    print('Tax rates used: Fed={}%, State={}%, Penalty={}%'.format(fed, state, penalty))


