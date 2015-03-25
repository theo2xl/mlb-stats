"""create source table

Revision ID: fe95f4615f
Revises: 177da7949d2d
Create Date: 2015-03-25 05:17:58.092408

"""

# revision identifiers, used by Alembic.
revision = 'fe95f4615f'
down_revision = '177da7949d2d'
branch_labels = None
depends_on = None

import datetime
from alembic import op
import sqlalchemy as sa

def upgrade():
    source = op.create_table('source',
        sa.Column('id', sa.Integer, sa.Sequence('source_seq_id', optional=True), primary_key=True),
        sa.Column('url', sa.String(255), nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.datetime.utcnow()))

    player_source = op.create_table('player_source',
        sa.Column('player_source_id', sa.Integer, primary_key=True),
        sa.Column('source_id', sa.Integer, sa.ForeignKey("source.id"), nullable=False),
        sa.Column('player_id', sa.Integer, sa.ForeignKey("player.id"), nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.datetime.utcnow()))

def downgrade():
    op.drop_table('player_source')
    op.drop_table('source')
