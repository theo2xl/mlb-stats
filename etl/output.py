import model

# outputs top 50 players by wOBA
# results will look like:
# 1 A McCutchen 0.4116
# 2 V Martinez 0.4114
# 3 J Abreu 0.4113
def print_woba_leaders(session):
    # fetch stats by wOBA descending
    woba_leaders_query = session.query(model.StatsYearBatting).order_by(model.StatsYearBatting.woba.desc())

    # track rank
    rk = 0

    # output header
    print '|Rk| Player Name   | wOBA |'
    print '---------------------------'

    # output player data
    for w in woba_leaders_query:
        rk+=1
        player_query = session.query(model.Player).filter(model.Player.id == w.player_id)
        for p in player_query:
            f = p.first_name
            l = p.last_name.ljust(13)
        woba = w.woba
        print(" {} {} {} {:.4f} ".format(str(rk).rjust(2),f,l,woba))
