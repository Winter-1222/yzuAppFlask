"""empty message

Revision ID: 7b5faa0bdb4e
Revises: acf527f39837
Create Date: 2024-05-12 17:34:58.795993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b5faa0bdb4e'
down_revision = 'acf527f39837'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('department', sa.String(length=100), nullable=False, comment='部门'))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('department')

    # ### end Alembic commands ###