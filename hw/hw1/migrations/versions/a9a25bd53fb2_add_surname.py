"""add_surname

Revision ID: a9a25bd53fb2
Revises: f4012dafaf2e
Create Date: 2026-10-07 12:03:38.489727

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a9a25bd53fb2'
down_revision: Union[str, Sequence[str], None] = 'f4012dafaf2e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
