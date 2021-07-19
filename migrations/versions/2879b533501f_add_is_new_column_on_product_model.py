"""Add 'is_new' column on Product model

Revision ID: 2879b533501f
Revises: a3c07cef11b3
Create Date: 2021-07-16 16:14:53.341006

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2879b533501f'
down_revision = 'a3c07cef11b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('is_new', sa.Boolean(), server_default='FALSE', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'is_new')
    # ### end Alembic commands ###
