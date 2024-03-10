"""update user table

Revision ID: 345283f3cec4
Revises: 0fa9d2ba4365
Create Date: 2024-03-10 13:26:24.230721

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '345283f3cec4'
down_revision = '0fa9d2ba4365'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=False))
        batch_op.drop_column('deleted_at')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('deleted_at', sa.DATETIME(), nullable=False))
        batch_op.drop_column('updated_at')

    # ### end Alembic commands ###
