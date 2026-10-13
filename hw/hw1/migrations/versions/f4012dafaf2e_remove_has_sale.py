"""remove_has_sale

Revision ID: f4012dafaf2e
Revises: b76c25884045
Create Date: 2026-10-07 12:02:21.387743

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f4012dafaf2e'
down_revision: Union[str, Sequence[str], None] = 'b76c25884045'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('patronymic', sa.String(length=50), nullable=True))

def downgrade() -> None:
    op.drop_column('users', 'patronymic')


