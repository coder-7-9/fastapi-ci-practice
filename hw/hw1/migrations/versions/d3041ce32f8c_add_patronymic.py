"""add_patronymic

Revision ID: d3041ce32f8c
Revises: a9a25bd53fb2
Create Date: 2026-10-07 12:05:25.156239

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "d3041ce32f8c"
down_revision: Union[str, Sequence[str], None] = "a9a25bd53fb2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
