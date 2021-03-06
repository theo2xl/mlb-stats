# Setup database models
# Use ORM for easier access to objects
# Could switch to a star schema (data warehouse) model if needed for performance.
import datetime
import urllib.request

from bs4 import BeautifulSoup
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# each table should have a created_at time
class TimestampMixin(object):
    created_at = Column(DateTime, default=datetime.datetime.utcnow())

class Team(TimestampMixin, Base):
    __tablename__ = 'team'

    id = Column(Integer, primary_key=True)
    location = Column(String)
    name = Column(String)
    abbr = Column(String)
    league = Column(String)

class Player(TimestampMixin, Base):
    __tablename__ = 'player'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    team_id = Column(Integer, ForeignKey("team.id"))
    position_id = Column(Integer, ForeignKey("position.id"))

    position = relationship("Position", backref="player")
    team = relationship("Team", backref="player")

class Source(TimestampMixin, Base):
    __tablename__ = 'source'

    id = Column(Integer, primary_key=True)
    url = Column(String)

    # when creating a new source, save the source and allow content to be accessed.
    def __init__(self, url):
        self.url = url
        self.created_at = datetime.datetime.utcnow()
        # this could be improved by saving to the same file type as the source url
        self.filename = 'source_'+self.created_at.strftime("%m-%d-%y_%H:%M:%S")+'.html'
        # immediately download file for tracking and more performant access
        self.download()
        self.content = self.content()

    # save file to local machine for history and safer access
    def download(self):
        urllib.request.urlretrieve(self.url, self.filename)

    # allow access to content of the downloaded file
    def content(self):
        leaderboard_soup = BeautifulSoup(open(self.filename))
        # this could be abstracted to allow for different source types
        soup = leaderboard_soup.html.body.table.tbody.find_all('tr')

        return soup

class PlayerSource(TimestampMixin, Base):
    __tablename__ = 'player_source'

    player_source_id = Column(Integer, primary_key=True)
    source_id = Column(Integer, ForeignKey("source.id"))
    player_id = Column(Integer, ForeignKey("player.id"))

class Position(TimestampMixin, Base):
    __tablename__ = 'position'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    abbr = Column(String)

class StatsYearBatting(TimestampMixin, Base):
    __tablename__ = 'stats_year_batting'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey("player.id"))
    year = Column(Integer)
    g = Column(Integer)
    pa = Column(Integer)
    ab = Column(Integer)
    r = Column(Integer)
    h = Column(Integer)
    s = Column(Integer)
    dbl = Column(Integer)
    tpl = Column(Integer)
    hr = Column(Integer)
    rbi = Column(Integer)
    bb = Column(Integer)
    ibb = Column(Integer)
    hbp = Column(Integer)
    so = Column(Integer)
    sb = Column(Integer)
    cs = Column(Integer)
    np = Column(Integer)
    sac = Column(Integer)
    sf = Column(Integer)
    tb = Column(Integer)
    gdp = Column(Integer)
    go = Column(Integer)
    ao = Column(Integer)
    xbh = Column(Integer)
    avg = Column(Float)
    obp = Column(Float)
    slg = Column(Float)
    ops = Column(Float)
    go_ao = Column(Float)
    woba = Column(Float)

    # create relationship so when querying stats you have access to player info as well
    player = relationship("Player", backref="stats_year_batting")
