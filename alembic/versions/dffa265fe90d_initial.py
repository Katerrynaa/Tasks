"""initial

Revision ID: dffa265fe90d
Revises: 
Create Date: 2024-01-18 13:14:35.146888

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "dffa265fe90d"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "departments",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column(
            "title",
            sa.String(200),
            sa.Column("country_name", sa.String(100)),
        ),
    )


def downgrade() -> None:
    op.drop_table("departments")
