"""empty message

Revision ID: 9c6aade89160
Revises: e327ca8c58e6
Create Date: 2022-08-12 02:20:45.458574

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c6aade89160'
down_revision = 'e327ca8c58e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('areas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('city', sa.String(length=2), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('venues', sa.Column('area_id', sa.Integer(), nullable=False))
    op.alter_column('venues', 'city',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.create_foreign_key(None, 'venues', 'areas', ['area_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'venues', type_='foreignkey')
    op.alter_column('venues', 'city',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('venues', 'area_id')
    op.drop_table('areas')
    # ### end Alembic commands ###
