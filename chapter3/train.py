"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import thinkplot
from chapter2.dice import Dice

FORMATS = ['png']


class Train(Dice):
    """Represents hypotheses about how many trains the company has.

    The likelihood function for the train problem is the same as
    for the Dice problem.
    """


def main():
    hypos = range(1, 1001)
    suite = Train(hypos)

    suite.Update(60)
    print(suite.Mean())

    thinkplot.PrePlot(1)
    thinkplot.Pmf(suite)
    thinkplot.Save(root='train1',
                   xlabel='Number of trains',
                   ylabel='Probability',
                   formats=FORMATS)


if __name__ == '__main__':
    main()
