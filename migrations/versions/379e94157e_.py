"""empty message

Revision ID: 379e94157e
Revises: 3385636b798c
Create Date: 2015-05-31 17:22:12.497687

"""

# revision identifiers, used by Alembic.
revision = '379e94157e'
down_revision = '3385636b798c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('github_url', sa.String(length=1000), nullable=True))
    op.drop_column('project', 'project_url')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('project_url', sa.VARCHAR(length=1000), autoincrement=False, nullable=True))
    op.drop_column('project', 'github_url')
    ### end Alembic commands ###
