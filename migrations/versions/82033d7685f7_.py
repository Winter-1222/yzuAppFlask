"""empty message

Revision ID: 82033d7685f7
Revises: d5f7c7d6e34a
Create Date: 2024-05-11 12:58:43.768593

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82033d7685f7'
down_revision = 'd5f7c7d6e34a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('suggestions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('student_id', sa.String(length=100), nullable=False, comment='学号'),
    sa.Column('title', sa.String(length=255), nullable=False, comment='意见标题'),
    sa.Column('is_public', sa.Boolean(), nullable=False, comment='是否公开'),
    sa.Column('contact', sa.String(length=100), nullable=False, comment='联系方式'),
    sa.Column('description', sa.Text(), nullable=False, comment='问题描述'),
    sa.Column('category_id', sa.Integer(), nullable=False, comment='分类ID'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('suggestions')
    # ### end Alembic commands ###
