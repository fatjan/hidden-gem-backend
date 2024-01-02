"""empty message

Revision ID: 429b0cc156dc
Revises: bdc6754af1fc
Create Date: 2024-01-02 14:53:34.253452

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '429b0cc156dc'
down_revision = 'bdc6754af1fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('role', sa.Enum('admin', 'user', name='userrole'), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('public_id'),
    sa.UniqueConstraint('username')
    )
    with op.batch_alter_table('review', schema=None) as batch_op:
        batch_op.alter_column('upvotes',
               existing_type=mysql.INTEGER(),
               nullable=True)
        batch_op.alter_column('downvotes',
               existing_type=mysql.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('review', schema=None) as batch_op:
        batch_op.alter_column('downvotes',
               existing_type=mysql.INTEGER(),
               nullable=False)
        batch_op.alter_column('upvotes',
               existing_type=mysql.INTEGER(),
               nullable=False)

    op.drop_table('user')
    # ### end Alembic commands ###