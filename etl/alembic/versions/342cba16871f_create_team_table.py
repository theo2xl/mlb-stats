"""create team table

Revision ID: 342cba16871f
Revises:
Create Date: 2015-03-23 23:04:24.289971

DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;
COMMENT ON SCHEMA public IS 'standard public schema';

"""

# revision identifiers, used by Alembic.
revision = '342cba16871f'
down_revision = None
branch_labels = None
depends_on = None

import datetime
from alembic import op
import sqlalchemy as sa


def upgrade():
    team = op.create_table('team',
        sa.Column('id', sa.Integer, sa.Sequence('team_seq_id', optional=True), primary_key=True),
        sa.Column('location', sa.String(30), nullable=False),
        sa.Column('name', sa.String(30), nullable=False),
        sa.Column('abbr', sa.String(3), nullable=False),
        sa.Column('league', sa.String(2), nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.datetime.utcnow())
    )

    op.bulk_insert(
    team,
    [
        {'location': 'Baltimore', 'name': 'Orioles', 'abbr': 'BAL', 'league': 'AL'},
        {'location': 'Boston', 'name': 'Red Sox', 'abbr': 'BOS', 'league': 'AL'},
        {'location': 'Chicago', 'name': 'White Sox', 'abbr': 'CWS', 'league': 'AL'},
        {'location': 'Cleveland', 'name': 'Indians', 'abbr': 'CLE', 'league': 'AL'},
        {'location': 'Detroit', 'name': 'Tigers', 'abbr': 'DET', 'league': 'AL'},
        {'location': 'Houston', 'name': 'Astros', 'abbr': 'HOU', 'league': 'AL'},
        {'location': 'Kansas City', 'name': 'Royals', 'abbr': 'KC', 'league': 'AL'},
        {'location': 'Los Angeles', 'name': 'Angels', 'abbr': 'LAA', 'league': 'AL'},
        {'location': 'Minnesota', 'name': 'Twins', 'abbr': 'MIN', 'league': 'AL'},
        {'location': 'New York', 'name': 'Yankees', 'abbr': 'NYY', 'league': 'AL'},
        {'location': 'Oakland', 'name': 'Athletics', 'abbr': 'OAK', 'league': 'AL'},
        {'location': 'Seattle', 'name': 'Mariners', 'abbr': 'SEA', 'league': 'AL'},
        {'location': 'Tampa Bay', 'name': 'Rays', 'abbr': 'TB', 'league': 'AL'},
        {'location': 'Texas', 'name': 'Rangers', 'abbr': 'TEX', 'league': 'AL'},
        {'location': 'Toronto', 'name': 'Blue Jays', 'abbr': 'TOR', 'league': 'AL'},
        {'location': 'Arizona', 'name': 'Diamondbacks', 'abbr': 'ARI', 'league': 'NL'},
        {'location': 'Atlanta', 'name': 'Braves', 'abbr': 'ATL', 'league': 'NL'},
        {'location': 'Chicago', 'name': 'Cubs', 'abbr': 'CHC', 'league': 'NL'},
        {'location': 'Cincinnati', 'name': 'Reds', 'abbr': 'CIN', 'league': 'NL'},
        {'location': 'Colorado', 'name': 'Rockies', 'abbr': 'COL', 'league': 'NL'},
        {'location': 'Los Angeles', 'name': 'Dodgers', 'abbr': 'LAD', 'league': 'NL'},
        {'location': 'Miami', 'name': 'Marlins', 'abbr': 'MIA', 'league': 'NL'},
        {'location': 'Milwaukee', 'name': 'Brewers', 'abbr': 'MIL', 'league': 'NL'},
        {'location': 'New York', 'name': 'Mets', 'abbr': 'NYM', 'league': 'NL'},
        {'location': 'Philadelphia', 'name': 'Phillies', 'abbr': 'PHI', 'league': 'NL'},
        {'location': 'Pittsburgh', 'name': 'Pirates', 'abbr': 'PIT', 'league': 'NL'},
        {'location': 'San Diego', 'name': 'Padres', 'abbr': 'SD', 'league': 'NL'},
        {'location': 'San Francisco', 'name': 'Giants', 'abbr': 'SF', 'league': 'NL'},
        {'location': 'St. Louis', 'name': 'Cardinals', 'abbr': 'STL', 'league': 'NL'},
        {'location': 'Washington', 'name': 'Nationals', 'abbr': 'WSH', 'league': 'NL'},
    ])

def downgrade():
    drop_table('team')
