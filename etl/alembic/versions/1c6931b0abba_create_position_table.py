"""create position table

Revision ID: 1c6931b0abba
Revises: 342cba16871f
Create Date: 2015-03-24 08:14:51.266042

"""

# revision identifiers, used by Alembic.
revision = '1c6931b0abba'
down_revision = '342cba16871f'
branch_labels = None
depends_on = None

import datetime
from alembic import op
import sqlalchemy as sa

def upgrade():
    position = op.create_table('position',
        sa.Column('id', sa.Integer, sa.Sequence('player_seq_id', optional=True), primary_key=True),
        sa.Column('name', sa.String(30), nullable=False),
        sa.Column('abbr', sa.String(2), nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.datetime.utcnow())
    )

    op.bulk_insert(
    position,
    [
        {'id':1, 'name':'Pitcher', 'abbr':'P'},
        {'id':2, 'name':'Catcher', 'abbr':'C'},
        {'id':3, 'name':'First Base', 'abbr':'1B'},
        {'id':4, 'name':'Second Base', 'abbr':'2B'},
        {'id':5, 'name':'Third Base', 'abbr':'3B'},
        {'id':6, 'name':'Shortstop', 'abbr':'SS'},
        {'id':7, 'name':'Left Field', 'abbr':'LF'},
        {'id':8, 'name':'Center Field', 'abbr':'CF'},
        {'id':9, 'name':'Right Field', 'abbr':'RF'},
        {'id':10, 'name':'Designated Hitter', 'abbr':'DH'},
    ])

def downgrade():
    drop_table('position')
