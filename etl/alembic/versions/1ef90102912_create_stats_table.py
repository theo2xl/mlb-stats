"""create stats table

Revision ID: 1ef90102912
Revises: fe95f4615f
Create Date: 2015-03-25 05:24:49.895637

"""

# revision identifiers, used by Alembic.
revision = '1ef90102912'
down_revision = 'fe95f4615f'
branch_labels = None
depends_on = None

import datetime
from alembic import op
import sqlalchemy as sa

def upgrade():
    stats_year_batting = op.create_table('stats_year_batting',
        sa.Column('id', sa.Integer, sa.Sequence('stats_year_batting_seq_id', optional=True), primary_key=True),
        sa.Column('player_id', sa.Integer, sa.ForeignKey('player.id')),
        sa.Column('year', sa.Integer),
        sa.Column('g', sa.Integer),
        sa.Column('pa', sa.Integer),
        sa.Column('ab', sa.Integer),
        sa.Column('r', sa.Integer),
        sa.Column('h', sa.Integer),
        sa.Column('s', sa.Integer),
        sa.Column('dbl', sa.Integer),
        sa.Column('tpl', sa.Integer),
        sa.Column('hr', sa.Integer),
        sa.Column('rbi', sa.Integer),
        sa.Column('bb', sa.Integer),
        sa.Column('ibb', sa.Integer),
        sa.Column('hbp', sa.Integer),
        sa.Column('so', sa.Integer),
        sa.Column('sb', sa.Integer),
        sa.Column('cs', sa.Integer),
        sa.Column('np', sa.Integer),
        sa.Column('sac', sa.Integer),
        sa.Column('sf', sa.Integer),
        sa.Column('tb', sa.Integer),
        sa.Column('gdp', sa.Integer),
        sa.Column('go', sa.Integer),
        sa.Column('ao', sa.Integer),
        sa.Column('xbh', sa.Integer),
        sa.Column('avg', sa.Float),
        sa.Column('obp', sa.Float),
        sa.Column('slg', sa.Float),
        sa.Column('ops', sa.Float),
        sa.Column('go_ao', sa.Float),
        sa.Column('woba', sa.Float),
        sa.Column('created_at', sa.DateTime, default=datetime.datetime.utcnow()))

def downgrade():
    op.drop_table('stats_year_batting')
