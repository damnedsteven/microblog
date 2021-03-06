"""empty message

Revision ID: d2c067cd6861
Revises: 8cc8b28a2554
Create Date: 2017-03-10 00:08:47.182617

"""

# revision identifiers, used by Alembic.
revision = 'd2c067cd6861'
down_revision = '8cc8b28a2554'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.DATETIME(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
