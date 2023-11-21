"""first migrations

Revision ID: 1900e2d04301
Revises: 
Create Date: 2023-11-16 21:31:33.386261

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1900e2d04301'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'departments',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('title', sa.String),
        sa.Column('country_name', sa.String),
    )

def downgrade() -> None:
    op.drop_table('departments')