"""create order_product table

Revision ID: 866eee13f60d
Revises: 16eca1cbe69e
Create Date: 2025-05-13 13:39:19.549379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '866eee13f60d'
down_revision = '16eca1cbe69e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('order_product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('order_product')
