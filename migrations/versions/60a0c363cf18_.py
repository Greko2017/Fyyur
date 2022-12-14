"""empty message

Revision ID: 60a0c363cf18
Revises: cd4404f7d4e0
Create Date: 2022-08-12 02:39:14.930504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60a0c363cf18'
down_revision = 'cd4404f7d4e0'
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
