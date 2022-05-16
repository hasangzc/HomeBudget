"""create budget table

Revision ID: 36eebf7e8f6e
Revises: 
Create Date: 2022-05-16 12:30:42.230518

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "36eebf7e8f6e"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "budget",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("daily_spending", sa.Integer(), nullable=False),
    )
    pass


def downgrade():
    op.drop_table("budget")
    pass
