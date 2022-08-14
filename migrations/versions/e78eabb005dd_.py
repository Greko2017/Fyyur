"""empty message

Revision ID: e78eabb005dd
Revises: 8ffbf116b2bd
Create Date: 2022-08-12 12:43:17.728731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e78eabb005dd'
down_revision = '8ffbf116b2bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artists', sa.Column('area_id', sa.Integer(), nullable=False))
    op.add_column('artists', sa.Column('address', sa.String(), nullable=False))
    op.add_column('artists', sa.Column('website_link', sa.String(), nullable=True))
    op.add_column('artists', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    op.add_column('artists', sa.Column('seeking_description', sa.String(), nullable=True))
    op.alter_column('artists', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('artists', 'phone',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.create_foreign_key(None, 'artists', 'areas', ['area_id'], ['id'])
    op.drop_column('artists', 'city')
    op.drop_column('artists', 'state')
    op.add_column('venues', sa.Column('genres', sa.ARRAY(sa.String()), nullable=True))
    op.alter_column('venues', 'area_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('venues', 'area_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('venues', 'genres')
    op.add_column('artists', sa.Column('state', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.add_column('artists', sa.Column('city', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'artists', type_='foreignkey')
    op.alter_column('artists', 'phone',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('artists', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('artists', 'seeking_description')
    op.drop_column('artists', 'seeking_talent')
    op.drop_column('artists', 'website_link')
    op.drop_column('artists', 'address')
    op.drop_column('artists', 'area_id')
    # ### end Alembic commands ###