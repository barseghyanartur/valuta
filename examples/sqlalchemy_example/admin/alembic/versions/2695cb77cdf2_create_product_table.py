"""create product table

Revision ID: 2695cb77cdf2
Revises: 
Create Date: 2021-07-03 00:08:14.129153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2695cb77cdf2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'product',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(64), nullable=False),
        sa.Column('price', sa.Integer),
        sa.Column('price_with_tax', sa.Integer),
        sa.Column('currency', sa.String(64), nullable=False),
    )


def downgrade():
    op.drop_table('product')
