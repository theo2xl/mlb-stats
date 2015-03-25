"""create player table

Revision ID: 177da7949d2d
Revises: 1c6931b0abba
Create Date: 2015-03-24 08:27:36.928767

"""

# revision identifiers, used by Alembic.
revision = '177da7949d2d'
down_revision = '1c6931b0abba'
branch_labels = None
depends_on = None

import datetime
from alembic import op
import sqlalchemy as sa

def upgrade():
    player = op.create_table('player',
        sa.Column('id', sa.Integer, sa.Sequence('player_seq_id', optional=True), primary_key=True),
        sa.Column('first_name', sa.String(30), nullable=True),
        sa.Column('last_name', sa.String(30), nullable=False),
        sa.Column('team_id', sa.Integer, sa.ForeignKey("team.id"), nullable=False),
        sa.Column('position_id', sa.Integer, sa.ForeignKey("position.id"), nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.datetime.utcnow()))

def downgrade():
    op.drop_table('player')
