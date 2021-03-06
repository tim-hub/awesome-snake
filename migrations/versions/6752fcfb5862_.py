"""empty message

Revision ID: 6752fcfb5862
Revises: 
Create Date: 2019-03-24 21:25:28.044698

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6752fcfb5862'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('game_uuid', sa.String(), nullable=False),
    sa.Column('game_info', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('game_uuid')
    )
    op.create_table('turn',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.Column('turn_uuid', sa.String(), nullable=False),
    sa.Column('turn_info', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.ForeignKeyConstraint(['game_id'], ['game.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('turn_uuid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('turn')
    op.drop_table('game')
    # ### end Alembic commands ###
