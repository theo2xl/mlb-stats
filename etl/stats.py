# calculate batting average
# number of hits per total at-bats
def avg(h, ab):
    return h / float(ab)

# calculate total bases
# sum each of the four different hit types
# multiplied by the number of bases covered
def tb(s, dbl, tpl, hr):
    return s + 2*dbl + 3*tpl + 4*hr

# caclulate on-base-percentage
# sum of the times a batter reach based skillfully (via a hit, walk or hit-by-pitch)
# divided by the number of plate appearances (minus sacrifice hits / bunts)
def obp(h, bb, hbp, ab, sf):
    return (h + bb + hbp) / float(ab + bb + sf + hbp)

# calculate slugging-percentage
# number of total bases achieved
# divided by the number of at-bats
def slg(tb, ab):
    return tb / float(ab)

# calculate on-base-plus-slugging
# sum of on-base-percentage and slugging
def ops(h, bb, hbp, ab, tb, sf):
    return obp(h, bb, hbp, ab, sf) + slg(tb, ab)

# calculate ground-ball to fly-ball ratio
def go_ao(go, ao):
    return go / float(ao)

# calculate weighted on-base average
# each year provides different weights
def woba_2014(bb, ibb, hbp, s, dbl, tpl, hr, ab, sf):
    bb_weight = 0.689
    hbp_weight = 0.722
    s_weight = 0.892
    dbl_weight = 1.283
    tpl_weight = 1.635
    hr_weight = 2.135

    return (bb_weight*(bb-ibb) +
            hbp_weight*hbp +
            s_weight*s +
            dbl_weight*dbl +
            tpl_weight*tpl +
            hr_weight*hr) / (ab + bb - ibb + sf + hbp)
