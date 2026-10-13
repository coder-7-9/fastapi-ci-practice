"""branch_test

Revision ID: bdf880219bdf
Revises: 948bde723b27
Create Date: 2026-10-07 12:09:34.048838

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bdf880219bdf'
down_revision: Union[str, Sequence[str], None] = 'd3041ce32f8c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('test_field', sa.String(length=50), nullable=True))



def downgrade() -> None:
    """Downgrade schema."""
    pass
