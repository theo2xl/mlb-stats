# etl.py
#
# extracts stastical HTML data from a URL
# parses and transforms to objects
# loads to a relational database
#
import requests
import model
import schema
import seed
import stats

from sqlalchemy import and_, create_engine, orm
from bs4 import BeautifulSoup

def source_url():
    return 'https://raw.githubusercontent.com/kruser/interview-developer/master/python/leaderboard.html'

def get_2014_batting_leaders():
    leaderboard = requests.get(source_url())
    leaderboard_soup = BeautifulSoup(leaderboard.content)
    soup = leaderboard_soup.html.body.table.tbody.find_all('tr')

    return soup

def load_source():
    new_source = model.Source(url = source_url())
    session.add(new_source)
    session.commit()

def load_player():
    for row in get_2014_batting_leaders():
        player_data = row.find_all('td')

        team_id = get_player_team_id(player_data[2].string)
        position_id = get_player_position_id(player_data[5].string)
        name = player_data[1].a.string.split(',')
        first_name = name[1].strip()
        last_name = name[0]

        new_player = model.Player(last_name = last_name,
                                  first_name = first_name,
                                  team_id = team_id,
                                  position_id = position_id)

        session.add(new_player)
        session.commit()

def load_player_source(source_id):
    for row in get_2014_batting_leaders():
        player_data = row.find_all('td')

        name = player_data[1].a.string.split(',')
        first_name = name[1].strip()
        last_name = name[0]
        player_id = get_player_source_id(first_name, last_name)

        new_player_source = model.PlayerSource(player_source_id = int(player_data[4].string),
                                               source_id = source_id,
                                               player_id = player_id)
        session.add(new_player_source)
        session.commit()

def load_stats(year):
    for row in get_2014_batting_leaders():
        player_data = row.find_all('td')

        player_id = get_player_id(int(player_data[4].string))

        g = int(player_data[6].string)
        pa = int(player_data[33].string)
        ab = int(player_data[7].string)
        r = int(player_data[8].string)
        h = int(player_data[9].string)
        dbl = int(player_data[10].string)
        tpl = int(player_data[11].string)
        hr = int(player_data[12].string)
        rbi = int(player_data[13].string)
        bb = int(player_data[14].string)
        ibb = int(player_data[22].string)
        hbp = int(player_data[23].string)
        so = int(player_data[15].string)
        sb = int(player_data[16].string)
        cs = int(player_data[17].string)
        np = int(player_data[32].string)
        sac = int(player_data[24].string)
        sf = int(player_data[25].string)
        gdp = int(player_data[28].string)
        go = int(player_data[29].string)
        ao = int(player_data[30].string)
        xbh = int(player_data[27].string)
        s = h - dbl - tpl - hr
        tb = stats.tb(s, dbl, tpl, hr)
        avg = stats.avg(h, ab)
        obp = stats.obp(h, bb, hbp, ab, sf)
        slg = stats.slg(tb, ab)
        ops = stats.ops(h, bb, hbp, ab, tb, sf)
        go_ao = stats.go_ao(go, ao)
        woba = stats.woba_2014(bb, ibb, hbp, s, dbl, tpl, hr, ab, sf)

        nbs = model.StatsYearBatting(player_id = player_id, year = year, g = g,
                                     pa = pa, ab = ab, r = r, h = h, s = s,
                                     dbl = dbl, tpl = tpl, hr = hr, rbi = rbi,
                                     bb = bb, ibb = ibb, hbp = hbp, so = so,
                                     sb = sb, cs = cs, np = np, sac = sac,
                                     sf = sf, tb = tb, gdp = gdp, go = go,
                                     ao = ao, xbh = xbh, avg = avg, obp = obp,
                                     slg = slg, ops = ops, go_ao = go_ao,
                                     woba = woba)
        session.add(nbs)

    session.commit()

def print_woba_leaders():
    woba_leaders_query = session.query(model.StatsYearBatting).order_by(model.StatsYearBatting.woba.desc())
    i = 0
    for w in woba_leaders_query:
        i+=1
        player_query = session.query(model.Player).filter(model.Player.id == w.player_id)
        for p in player_query:
            f = p.first_name
            l = p.last_name
        woba = w.woba
        print("{} {} {} {:.4f}".format(str(i),f,l,woba))

def get_player_id(player_source_id):
    player_id_query = session.query(model.PlayerSource.player_id).filter(model.PlayerSource.player_source_id == player_source_id)
    for pid in player_id_query:
        player_id = pid[0]
    return player_id

def get_player_team_id(team_abbr):
    player_team_id_query = session.query(model.Team.id).filter(model.Team.abbr == team_abbr)
    for team in player_team_id_query:
        team_id = team[0]
    return team_id

def get_player_position_id(position_abbr):
    player_pos_id_query = session.query(model.Position.id).filter(model.Position.abbr == position_abbr)
    for pos in player_pos_id_query:
        pos_id = pos[0]
    return pos_id

def get_player_source_id(first_name, last_name):
    player_id_query = session.query(model.Player.id).filter(and_(model.Player.last_name == last_name,
                                                                 model.Player.first_name == first_name))
    for pid in player_id_query:
        player_id = pid[0]
    return player_id

# Create an engine and create all the tables we need
engine = create_engine('sqlite:///:memory:', echo=False)
schema.metadata.bind = engine
schema.metadata.create_all()

# Set up the session
sm = orm.sessionmaker(bind=engine, autoflush=True, autocommit=False,
    expire_on_commit=True)
session = orm.scoped_session(sm)

# seed db
seed.team(session)
seed.position(session)

# load db
load_source()
load_player()
load_player_source(1)
load_stats(2014)

# output solution
print_woba_leaders()
