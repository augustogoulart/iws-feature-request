"""empty message

Revision ID: 33bfab617ac8
Revises: 
Create Date: 2017-09-20 15:36:49.566367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33bfab617ac8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_area',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('feature_request',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=250), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('target_date', sa.DateTime(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('product_area_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['product_area_id'], ['product_area.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('feature_request')
    op.drop_table('product_area')
    op.drop_table('client')
    # ### end Alembic commands ###
