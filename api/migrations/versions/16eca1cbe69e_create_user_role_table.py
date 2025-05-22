"""create user_role table

Revision ID: 16eca1cbe69e
Revises: cdc7d4ab63a9
Create Date: 2025-05-13 13:35:28.714560

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16eca1cbe69e'
down_revision = 'cdc7d4ab63a9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user_order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('user_order')
