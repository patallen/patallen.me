"""empty message

Revision ID: 38d5248387e3
Revises: 379e94157e
Create Date: 2015-07-18 01:28:18.375969

"""

# revision identifiers, used by Alembic.
revision = '38d5248387e3'
down_revision = '379e94157e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('live_url', sa.String(length=1000), nullable=True))
    op.add_column('project', sa.Column('order_num', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('project', 'order_num')
    op.drop_column('project', 'live_url')
    ### end Alembic commands ###
