"""empty message

Revision ID: 5d96feeaa071
Revises: c0462c7460e9
Create Date: 2022-08-13 17:02:53.400190

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d96feeaa071'
down_revision = 'c0462c7460e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shows', sa.Column('start_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('shows', 'start_time')
    # ### end Alembic commands ###