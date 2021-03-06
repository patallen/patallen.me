"""empty message

Revision ID: 16f868a38787
Revises: None
Create Date: 2015-05-19 15:06:14.636653

"""

# revision identifiers, used by Alembic.
revision = '16f868a38787'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nickname', sa.String(length=60), nullable=True),
    sa.Column('first_name', sa.String(length=60), nullable=False),
    sa.Column('last_name', sa.String(length=60), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('location', sa.String(length=60), nullable=True),
    sa.Column('authenticated', sa.Boolean(), nullable=True),
    sa.Column('pw_hash', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nickname')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author', sa.Integer(), nullable=True),
    sa.Column('slug', sa.String(), nullable=True),
    sa.Column('title', sa.String(length=240), nullable=False),
    sa.Column('body_md', sa.String(), nullable=False),
    sa.Column('body_html', sa.String(), nullable=True),
    sa.Column('excerpt', sa.String(length=600), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_updated', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('stack', sa.String(length=1000), nullable=True),
    sa.Column('project_url', sa.String(length=1000), nullable=True),
    sa.Column('img_url', sa.String(length=300), nullable=True),
    sa.Column('date_completed', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['owner'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('project')
    op.drop_table('post')
    op.drop_table('user')
    ### end Alembic commands ###
