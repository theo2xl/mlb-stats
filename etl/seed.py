# seed db with static teams and positions
import model

def team(session):
    session.add_all([
        model.Team(location='Baltimore', name='Orioles', abbr='BAL', league='AL'),
        model.Team(location='Boston', name='Red Sox', abbr='BOS', league='AL'),
        model.Team(location='Chicago', name='White Sox', abbr='CWS', league='AL'),
        model.Team(location='Cleveland', name='Indians', abbr='CLE', league='AL'),
        model.Team(location='Detroit', name='Tigers', abbr='DET', league='AL'),
        model.Team(location='Houston', name='Astros', abbr='HOU', league='AL'),
        model.Team(location='Kansas City', name='Royals', abbr='KC', league='AL'),
        model.Team(location='Los Angeles', name='Angels', abbr='LAA', league='AL'),
        model.Team(location='Minnesota', name='Twins', abbr='MIN', league='AL'),
        model.Team(location='New York', name='Yankees', abbr='NYY', league='AL'),
        model.Team(location='Oakland', name='Athletics', abbr='OAK', league='AL'),
        model.Team(location='Seattle', name='Mariners', abbr='SEA', league='AL'),
        model.Team(location='Tampa Bay', name='Rays', abbr='TB', league='AL'),
        model.Team(location='Texas', name='Rangers', abbr='TEX', league='AL'),
        model.Team(location='Toronto', name='Blue Jays', abbr='TOR', league='AL'),
        model.Team(location='Arizona', name='Diamondbacks', abbr='ARI', league='NL'),
        model.Team(location='Atlanta', name='Braves', abbr='ATL', league='NL'),
        model.Team(location='Chicago', name='Cubs', abbr='CHC', league='NL'),
        model.Team(location='Cincinnati', name='Reds', abbr='CIN', league='NL'),
        model.Team(location='Colorado', name='Rockies', abbr='COL', league='NL'),
        model.Team(location='Los Angeles', name='Dodgers', abbr='LAD', league='NL'),
        model.Team(location='Miami', name='Marlins', abbr='MIA', league='NL'),
        model.Team(location='Milwaukee', name='Brewers', abbr='MIL', league='NL'),
        model.Team(location='New York', name='Mets', abbr='NYM', league='NL'),
        model.Team(location='Philadelphia', name='Phillies', abbr='PHI', league='NL'),
        model.Team(location='Pittsburgh', name='Pirates', abbr='PIT', league='NL'),
        model.Team(location='San Diego', name='Padres', abbr='SD', league='NL'),
        model.Team(location='San Francisco', name='Giants', abbr='SF', league='NL'),
        model.Team(location='St. Louis', name='Cardinals', abbr='STL', league='NL'),
        model.Team(location='Washington', name='Nationals', abbr='WSH', league='NL')])
    session.commit()

def position(session):
    session.add_all([
        model.Position(id=1, name='Pitcher', abbr='P'),
        model.Position(id=2, name='Catcher', abbr='C'),
        model.Position(id=3, name='First Base', abbr='1B'),
        model.Position(id=4, name='Second Base', abbr='2B'),
        model.Position(id=5, name='Third Base', abbr='3B'),
        model.Position(id=6, name='Shortstop', abbr='SS'),
        model.Position(id=7, name='Left Field', abbr='LF'),
        model.Position(id=8, name='Center Field', abbr='CF'),
        model.Position(id=9, name='Right Field', abbr='RF'),
        model.Position(id=10, name='Designated Hitter', abbr='DH')])
    session.commit()
