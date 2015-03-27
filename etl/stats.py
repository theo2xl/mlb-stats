def avg(h, ab):
    """avg

    calculate batting average
    number of hits per total at-bats

    >>> avg(4, 10)
    0.4
    """
    return h / float(ab)

def tb(s, dbl, tpl, hr):
    """tb

    calculate total bases
    sum each of the four different hit types
    multiplied by the number of bases covered

    >>> tb(1, 1, 1, 1)
    10
    """
    return s + 2*dbl + 3*tpl + 4*hr

def obp(h, bb, hbp, ab, sf):
    """obp

    caclulate on-base-percentage
    sum of the times a batter reach based skillfully (via a hit, walk or hit-by-pitch)
    divided by the number of plate appearances (minus sacrifice hits / bunts)

    >>> obp(1, 1, 1, 3, 1)
    0.5
    """
    return (h + bb + hbp) / float(ab + bb + sf + hbp)

def slg(tb, ab):
    """slg

    calculate slugging-percentage
    number of total bases achieved
    divided by the number of at-bats

    >>> slg(5, 10)
    0.5
    """
    return tb / float(ab)

def ops(h, bb, hbp, ab, tb, sf):
    """ops

    calculate on-base-plus-slugging
    sum of on-base-percentage and slugging

    >>> ops(1, 1, 1, 3, 3, 1)
    1.5
    """
    return obp(h, bb, hbp, ab, sf) + slg(tb, ab)

def go_ao(go, ao):
    """go_ao

    calculate ground-ball to fly-ball ratio

    >>> go_ao(2, 1)
    2.0
    """
    return go / float(ao)

def woba(yr, bb, ibb, hbp, s, dbl, tpl, hr, ab, sf):
    """woba

    calculate weighted on-base average
    each year provides different weights

    Anthony Rizzo's 2014 wOBA was 0.397

    >>> woba(2014, 73, 7, 15, 89, 28, 1, 32, 524, 4)
    0.39666830870279146
    """

    # woba_weights dictionary
    # key: year
    # value: tuple of weights: bb, hbp, s, dbl, tpl, hr
    #
    # note: currenlty only 2014 is loaded as that is all that is needed for this project
    woba_weights = { '2014': (0.689, 0.722, 0.892, 1.283, 1.635, 2.135) }

    weight = woba_weights[str(yr)]

    return (weight[0]*(bb-ibb) +
            weight[1]*hbp +
            weight[2]*s +
            weight[3]*dbl +
            weight[4]*tpl +
            weight[5]*hr) / (ab + bb - ibb + sf + hbp)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
