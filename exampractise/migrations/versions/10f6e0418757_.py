"""empty message

Revision ID: 10f6e0418757
Revises:
Create Date: 2023-04-12 19:30:11.969047

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "10f6e0418757"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("username", sa.String(length=120), nullable=True),
        sa.Column("email", sa.String(length=120), nullable=True),
        sa.Column("firstname", sa.String(length=120), nullable=True),
        sa.Column("lastname", sa.String(length=120), nullable=True),
        sa.Column("password", sa.String(length=255), nullable=True),
        sa.Column(
            "usertype",
            sa.Enum("STUDENT", "ADMIN", name="usertype"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("username"),
    )
    op.create_table(
        "auth_token",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("token", sa.String(length=255), nullable=True),
        sa.Column("expiry_time", sa.Integer(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.username"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("auth_token")
    op.drop_table("user")
    # ### end Alembic commands ###
