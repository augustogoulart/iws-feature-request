"""empty message

Revision ID: 742d67aa10b4
Revises: 
Create Date: 2017-09-22 16:35:40.578223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '742d67aa10b4'
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
    op.create_table('priority',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('feature_request',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('target_date', sa.String(), nullable=False),
    sa.Column('product_area', sa.String(), nullable=False),
    sa.Column('priority', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), server_default='0', nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('feature_request')
    op.drop_table('priority')
    op.drop_table('client')
    # ### end Alembic commands ###
