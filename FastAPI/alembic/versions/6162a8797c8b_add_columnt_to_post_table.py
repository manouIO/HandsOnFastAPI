"""add columnt to post table

Revision ID: 6162a8797c8b
Revises: 7ad37b27ea13
Create Date: 2026-02-04 10:13:43.588160

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6162a8797c8b'
down_revision: Union[str, Sequence[str], None] = '7ad37b27ea13'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'created_at')   
    pass
