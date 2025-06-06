"""Price to token

Revision ID: 5c39746c4a4a
Revises: b6e3e806bf85
Create Date: 2025-06-04 11:02:30.965497

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5c39746c4a4a'
down_revision = 'b6e3e806bf85'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tokens', sa.Integer(), nullable=False))
        batch_op.drop_column('price')

    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tokens', sa.Integer(), nullable=False))
        batch_op.drop_column('price')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price', mysql.FLOAT(), nullable=False))
        batch_op.drop_column('tokens')

    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price', mysql.FLOAT(), nullable=False))
        batch_op.drop_column('tokens')

    # ### end Alembic commands ###
