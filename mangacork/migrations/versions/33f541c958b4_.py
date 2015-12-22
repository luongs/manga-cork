"""empty message

Revision ID: 33f541c958b4
Revises: None
Create Date: 2015-12-21 16:32:49.426290

"""

# revision identifiers, used by Alembic.
revision = '33f541c958b4'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('lastpage',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('lastpage', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'lastpage_pkey'),
    sa.UniqueConstraint('lastpage', name=u'lastpage_lastpage_key')
    )
    ### end Alembic commands ###


def downgrade():
    op.drop_table('lastpage')
    ### end Alembic commands ###
