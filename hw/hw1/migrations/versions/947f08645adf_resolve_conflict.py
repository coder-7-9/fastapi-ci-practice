"""resolve_conflict

Revision ID: 947f08645adf
Revises: 948bde723b27, bdf880219bdf
Create Date: 2026-10-07 12:11:09.963573

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "947f08645adf"
down_revision: Union[str, Sequence[str], None] = ("948bde723b27", "bdf880219bdf")
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
