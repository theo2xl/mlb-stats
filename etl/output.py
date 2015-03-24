import model

# outputs top 50 players by wOBA
# results will look like:
# |Rk|Tm |Po| Player Name   | wOBA |
#  --------------------------------
#   1 PIT CF A McCutchen     0.4116
#   2 DET DH V Martinez      0.4114
#   3 CWS 1B J Abreu         0.4113
#   4 MIA RF G Stanton       0.4031
#   5 LAA CF M Trout         0.4024
def print_woba_leaders(session):
    # fetch stats by wOBA descending
    woba_leaders_query = (session
                          .query(model.StatsYearBatting)
                          .order_by(model.StatsYearBatting.woba.desc()))

    # track rank
    rk = 0

    # output header
    print('|Rk|Tm |Po| Player Name   | wOBA |')
    print(' --------------------------------')

    # output player data
    for w in woba_leaders_query:
        rk+=1
        f = w.player.first_name
        l = w.player.last_name
        t = w.player.team.abbr
        p = w.player.position.abbr
        woba = w.woba
        print(" {} {} {} {} {} {:.4f} ".format(str(rk).rjust(2),
                                               t.rjust(3),
                                               p.rjust(2),
                                               f,
                                               l.ljust(13),
                                               woba))
