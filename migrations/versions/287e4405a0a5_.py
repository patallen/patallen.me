"""empty message

Revision ID: 287e4405a0a5
Revises: 5754bfe1a45f
Create Date: 2015-08-11 15:07:25.561247

"""

# revision identifiers, used by Alembic.
revision = '287e4405a0a5'
down_revision = '5754bfe1a45f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('blog_post_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'project', 'post', ['blog_post_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'project', type_='foreignkey')
    op.drop_column('project', 'blog_post_id')
    ### end Alembic commands ###
