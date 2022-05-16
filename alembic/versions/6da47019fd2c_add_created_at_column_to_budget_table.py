"""add created_at column to budget table

Revision ID: 6da47019fd2c
Revises: 36eebf7e8f6e
Create Date: 2022-05-16 12:43:01.846856

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6da47019fd2c"
down_revision = "36eebf7e8f6e"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "budget",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )
    pass


def downgrade():
    op.drop_column("budget")
    pass
