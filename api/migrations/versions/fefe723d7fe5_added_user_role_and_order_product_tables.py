"""Added user_role and order_product tables

Revision ID: fefe723d7fe5
Revises: 4e084a523c35
Create Date: 2025-05-11 12:49:33.471924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fefe723d7fe5'
down_revision = '4e084a523c35'
branch_labels = None
depends_on = None


def upgrade():
    # op.create_table('user_role',
    # sa.Column('id', sa.Integer(), nullable=False),
    # sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
    # sa.Column('role_id', sa.Integer(), nullable=False),
    # sa.Column('created_at', sa.DateTime(), nullable=False),
    # sa.Column('updated_at', sa.DateTime(), nullable=True),
    # sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    # sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    # sa.PrimaryKeyConstraint('id')
    # )
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
    op.drop_table('user_role')
    op.drop_table('order_product')
