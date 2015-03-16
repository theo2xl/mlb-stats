# etl.py
#
# extracts tabular HTML baseball batting data from a URL
# parses and transforms data to objects
# loads to a relational database
# prints out rankings based on wOBA
#
import model
import schema
import seed
import source
import stats

from sqlalchemy import create_engine, orm

def print_woba_leaders():
    woba_leaders_query = session.query(model.StatsYearBatting).order_by(model.StatsYearBatting.woba.desc())
    rk = 0
    for w in woba_leaders_query:
        rk+=1
        player_query = session.query(model.Player).filter(model.Player.id == w.player_id)
        for p in player_query:
            f = p.first_name
            l = p.last_name
        woba = w.woba
        print("{} {} {} {:.4f}".format(str(rk),f,l,woba))

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
source.load_source(session)
source.load_player(session)
source.load_player_source(session, 1)
source.load_stats(session, 2014)

# output solution
print_woba_leaders()
