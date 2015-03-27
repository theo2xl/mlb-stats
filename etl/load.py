import model
import stats

import datetime
from sqlalchemy import and_, create_engine, orm
from bs4 import BeautifulSoup

# given a url:
# * create a new source in the database
# * download the source locally
# * return source and content for future parsing
def source(session, url):
    new_source = model.Source(url)
    session.add(new_source)
    session.commit()

    return new_source

# load all players from a given source
def player(session, content):
    for row in content:
        player_data = row.find_all('td')
        first_name, last_name = _get_first_name_last_name(player_data[1].a)

        new_player = {'first_name': first_name,
                      'last_name': last_name,
                      'team_id': _get_player_team_id(session, player_data[2].string),
                      'position_id': _get_player_position_id(session, player_data[5].string)}

        session.add(model.Player(**new_player))
        session.commit()

# load player source relationship
# given a player's source id, it should map to our player db id
def player_source(session, source):
    for row in source.content:
        player_data = row.find_all('td')
        source_player_id = int(player_data[4].string)
        first_name, last_name = _get_first_name_last_name(player_data[1].a)

        new_player_source = {'player_source_id': source_player_id,
                             'source_id': source.id,
                             'player_id': _get_player_source_id(session, first_name, last_name)}

        session.add(model.PlayerSource(**new_player_source))
        session.commit()

# load player's batting stats
# we load calculated statistics to improve read speed at the cost of db size
def batting_stats(session, year, content):
    for row in content:
        player_data = row.find_all('td')
        source_player_id = int(player_data[4].string)

        # store simplest data without calculations in a dictionary
        pdata = {'player_id': _get_player_id(session, source_player_id),
                 'g': int(player_data[6].string),
                 'pa': int(player_data[33].string),
                 'ab': int(player_data[7].string),
                 'r': int(player_data[8].string),
                 'h': int(player_data[9].string),
                 'dbl': int(player_data[10].string),
                 'tpl': int(player_data[11].string),
                 'hr': int(player_data[12].string),
                 'rbi': int(player_data[13].string),
                 'bb': int(player_data[14].string),
                 'ibb': int(player_data[22].string),
                 'hbp': int(player_data[23].string),
                 'so': int(player_data[15].string),
                 'sb': int(player_data[16].string),
                 'cs': int(player_data[17].string),
                 'np': int(player_data[32].string),
                 'sac': int(player_data[24].string),
                 'sf': int(player_data[25].string),
                 'gdp': int(player_data[28].string),
                 'go': int(player_data[29].string),
                 'ao': int(player_data[30].string),
                 'xbh': int(player_data[27].string)}

        # do calculations for singles and total bases for future calculations
        singles = pdata['h'] - pdata['dbl'] - pdata['tpl'] - pdata['hr']
        total_bases = stats.tb(singles, pdata['dbl'], pdata['tpl'], pdata['hr'])

        # create second dictionary to be merged into initial dictionary
        # use our custom stats file to calculate baseball values
        calc_stats = {'s': singles,
                      'tb': total_bases,
                      'avg': stats.avg(pdata['h'], pdata['ab']),
                      'obp': stats.obp(pdata['h'], pdata['bb'], pdata['hbp'],
                                       pdata['ab'], pdata['sf']),
                      'slg': stats.slg(total_bases, pdata['ab']),
                      'ops': stats.ops(pdata['h'], pdata['bb'], pdata['hbp'],
                             pdata['ab'], total_bases, pdata['sf']),
                      'go_ao': stats.go_ao(pdata['go'], pdata['ao']),
                      'woba': stats.woba(year, pdata['bb'], pdata['ibb'],
                                         pdata['hbp'], singles, pdata['dbl'],
                                         pdata['tpl'], pdata['hr'], pdata['ab'],
                                         pdata['sf'])}

        # merge two dictionaries for creation of new batting stats object
        new_batting_stats = pdata.copy()
        new_batting_stats.update(calc_stats)

        session.add(model.StatsYearBatting(**new_batting_stats))

    session.commit()

def _get_player_id(session, player_source_id):
    player_id_query = session.query(model.PlayerSource.player_id).filter(model.PlayerSource.player_source_id == player_source_id)
    for pid in player_id_query:
        player_id = pid[0]
    return player_id

def _get_player_team_id(session, team_abbr):
    player_team_id_query = session.query(model.Team.id).filter(model.Team.abbr == team_abbr)
    for team in player_team_id_query:
        team_id = team[0]
    return team_id

def _get_player_position_id(session, position_abbr):
    player_pos_id_query = session.query(model.Position.id).filter(model.Position.abbr == position_abbr)
    for pos in player_pos_id_query:
        pos_id = pos[0]
    return pos_id

def _get_player_source_id(session, first_name, last_name):
    player_id_query = session.query(model.Player.id).filter(and_(model.Player.last_name == last_name,
                                                                 model.Player.first_name == first_name))
    for pid in player_id_query:
        player_id = pid[0]
    return player_id

# player's full name is stored in the second td as an achor 'last_name, first_initial'
def _get_first_name_last_name(full_name):
    names = full_name.string.split(',')
    return names[1].strip(), names[0]
