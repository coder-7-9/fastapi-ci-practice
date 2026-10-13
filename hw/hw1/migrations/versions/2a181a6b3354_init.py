"""init

Revision ID: 2a181a6b3354
Revises: 8055df67e459
Create Date: 2026-10-07 12:00:58.337103

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2a181a6b3354'
down_revision: Union[str, Sequence[str], None] = '8055df67e459'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('has_sale', sa.Boolean(), nullable=True)
    )

def downgrade() -> None:
    op.drop_table('users')
