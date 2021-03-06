"""empty message

Revision ID: 957e941ac1d2
Revises: 1804fff17429
Create Date: 2018-11-14 20:55:41.888307

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '957e941ac1d2'
down_revision = '1804fff17429'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('grade',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('stu',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('grade_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['grade_id'], ['grade.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stu')
    op.drop_table('grade')
    # ### end Alembic commands ###
