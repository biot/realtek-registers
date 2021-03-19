"""Add table description

Revision ID: 3a9e5c60f9a7
Revises: 58fe24dc22a3
Create Date: 2021-03-20 21:55:25.524702

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a9e5c60f9a7'
down_revision = '58fe24dc22a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('access_type', sa.Integer(), nullable=False),
    sa.Column('size', sa.Integer(), nullable=False),
    sa.Column('family_id', sa.Integer(), nullable=False),
    sa.Column('feature_id', sa.Integer(), nullable=False),
    sa.Column('ctrl_register_id', sa.Integer(), nullable=False),
    sa.Column('data_register_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['ctrl_register_id'], ['register.id'], ),
    sa.ForeignKeyConstraint(['data_register_id'], ['register.id'], ),
    sa.ForeignKeyConstraint(['family_id'], ['family.id'], ),
    sa.ForeignKeyConstraint(['feature_id'], ['feature.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('family_id', 'name', name='u_family_table')
    )
    op.create_table('table_field',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('lsb', sa.Integer(), nullable=False),
    sa.Column('size', sa.Integer(), nullable=False),
    sa.Column('table_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['table_id'], ['table.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('table_id', 'lsb', name='u_table_field')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('table_field')
    op.drop_table('table')
    # ### end Alembic commands ###
