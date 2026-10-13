"""remove_has_sale

Revision ID: b76c25884045
Revises: 2a181a6b3354
Create Date: 2026-10-07 12:02:05.129069

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b76c25884045'
down_revision: Union[str, Sequence[str], None] = '2a181a6b3354'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
