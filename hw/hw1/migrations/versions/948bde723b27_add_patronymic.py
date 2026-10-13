"""add_patronymic

Revision ID: 948bde723b27
Revises: d3041ce32f8c
Create Date: 2026-10-07 12:07:24.218897

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "948bde723b27"
down_revision: Union[str, Sequence[str], None] = "d3041ce32f8c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
