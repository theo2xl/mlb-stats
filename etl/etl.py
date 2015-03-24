# etl.py
#
# extracts tabular HTML baseball batting data from a URL
# parses and transforms data to objects
# loads to a relational database
# prints out rankings based on wOBA
#
import load
import model
import output
import schema
import stats

from sqlalchemy import create_engine, orm

# Create an engine and create all the tables we need
# This is currently done with a sqlite in memory db.
# Just need to replace line 31 with real db
engine = create_engine('postgresql+psycopg2://postgres:postgres@db', echo=False)
schema.metadata.bind = engine
schema.metadata.create_all()

# Set up the session
sm = orm.sessionmaker(bind=engine, autoflush=True, autocommit=False,
    expire_on_commit=True)
session = orm.scoped_session(sm)

# load db
batting_leaders = load.source(session, 'https://raw.githubusercontent.com/kruser/interview-developer/master/python/leaderboard.html')
load.player(session, batting_leaders.content)
load.player_source(session, batting_leaders)
load.batting_stats(session, 2014, batting_leaders.content)

# output solution
output.print_woba_leaders(session)
