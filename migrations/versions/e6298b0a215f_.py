"""empty message

Revision ID: e6298b0a215f
Revises: 60a0c363cf18
Create Date: 2022-08-12 02:39:59.324563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6298b0a215f'
down_revision = '60a0c363cf18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('areas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('venues', 'city',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('venues', 'city',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_table('areas')
    # ### end Alembic commands ###
