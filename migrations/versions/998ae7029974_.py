"""empty message

Revision ID: 998ae7029974
Revises: 82033d7685f7
Create Date: 2024-05-11 13:25:13.441308

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '998ae7029974'
down_revision = '82033d7685f7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('suggestions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=False, comment='创建时间'))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('suggestions', schema=None) as batch_op:
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###
