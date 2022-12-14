"""empty message

Revision ID: 60d9388f50cc
Revises: e6298b0a215f
Create Date: 2022-08-12 02:41:42.962272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60d9388f50cc'
down_revision = 'e6298b0a215f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('areas', sa.Column('state', sa.String(), nullable=True))
    op.drop_column('areas', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('areas', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('areas', 'state')
    # ### end Alembic commands ###
