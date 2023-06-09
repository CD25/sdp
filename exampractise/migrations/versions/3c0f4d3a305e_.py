"""empty message

Revision ID: 3c0f4d3a305e
Revises: 
Create Date: 2023-04-12 14:13:56.851360

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c0f4d3a305e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=120), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('firstname', sa.String(length=120), nullable=True),
    sa.Column('lastname', sa.String(length=120), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('usertype', sa.Enum('STUDENT', 'ADMIN', name='usertype'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('user_token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=255), nullable=True),
    sa.Column('expiry_time', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_token')
    op.drop_table('user')
    # ### end Alembic commands ###
