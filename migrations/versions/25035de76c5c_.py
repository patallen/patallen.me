"""empty message

Revision ID: 25035de76c5c
Revises: 355b4e311a22
Create Date: 2015-08-13 21:33:42.162986

"""

# revision identifiers, used by Alembic.
revision = '25035de76c5c'
down_revision = '355b4e311a22'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('slug', sa.String(length=64), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('project', 'slug')
    ### end Alembic commands ###