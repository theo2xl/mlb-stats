# Schema for our new database tables
import datetime
from sqlalchemy import *

metadata = MetaData()

# used in saving created_at and updated_at datetimes
def now():
    return datetime.datetime.utcnow()

player = Table('player', metadata,
    Column('id', Integer, Sequence('player_seq_id', optional=True), primary_key=True),
    Column('first_name', String(30), nullable=True),
    Column('last_name', String(30), nullable=False),
    Column('team_id', Integer, ForeignKey("team.id"), nullable=False),
    Column('position_id', Integer, ForeignKey("position.id"), nullable=False),
    Column('created_at', DateTime, default=now)
)

player_source = Table('player_source', metadata,
    Column('player_source_id', Integer, primary_key=True),
    Column('source_id', Integer, ForeignKey("source.id"), nullable=False),
    Column('player_id', Integer, ForeignKey("player.id"), nullable=False),
    Column('created_at', DateTime, default=now)
)

position = Table('position', metadata,
    Column('id', Integer, Sequence('position_seq_id', optional=True), primary_key=True),
    Column('name', String(30), nullable=False),
    Column('abbr', String(2), nullable=False),
    Column('created_at', DateTime, default=now)
)

source = Table('source', metadata,
    Column('id', Integer, Sequence('source_seq_id', optional=True), primary_key=True),
    Column('url', String(255), nullable=False),
    Column('created_at', DateTime, default=now)
)

stats_year_batting = Table('stats_year_batting', metadata,
    Column('id', Integer, Sequence('stats_year_batting_seq_id', optional=True), primary_key=True),
    Column('player_id', Integer, ForeignKey('player.id')),
    Column('year', Integer),
    Column('g', Integer),
    Column('pa', Integer),
    Column('ab', Integer),
    Column('r', Integer),
    Column('h', Integer),
    Column('s', Integer),
    Column('dbl', Integer),
    Column('tpl', Integer),
    Column('hr', Integer),
    Column('rbi', Integer),
    Column('bb', Integer),
    Column('ibb', Integer),
    Column('hbp', Integer),
    Column('so', Integer),
    Column('sb', Integer),
    Column('cs', Integer),
    Column('np', Integer),
    Column('sac', Integer),
    Column('sf', Integer),
    Column('tb', Integer),
    Column('gdp', Integer),
    Column('go', Integer),
    Column('ao', Integer),
    Column('xbh', Integer),
    Column('avg', Float),
    Column('obp', Float),
    Column('slg', Float),
    Column('ops', Float),
    Column('go_ao', Float),
    Column('woba', Float),
    Column('created_at', DateTime)
)

team = Table('team', metadata,
    Column('id', Integer, Sequence('team_seq_id', optional=True), primary_key=True),
    Column('location', String(30), nullable=False),
    Column('name', String(30), nullable=False),
    Column('abbr', String(3), nullable=False),
    Column('league', String(2), nullable=False),
    Column('created_at', DateTime, default=now)
)
