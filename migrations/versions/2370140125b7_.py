"""empty message

Revision ID: 2370140125b7
Revises: 32e1cd1d94de
Create Date: 2015-05-19 19:07:00.216730

"""

# revision identifiers, used by Alembic.
revision = '2370140125b7'
down_revision = '32e1cd1d94de'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=240), nullable=True),
    sa.Column('name', sa.String(length=60), nullable=False),
    sa.Column('slug', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    op.add_column(u'post', sa.Column('category_id', sa.Integer(), nullable=True))
    op.create_unique_constraint(None, 'post', ['slug'])
    op.create_foreign_key(None, 'post', 'category', ['category_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.drop_constraint(None, 'post', type_='unique')
    op.drop_column(u'post', 'category_id')
    op.drop_table('category')
    ### end Alembic commands ###
