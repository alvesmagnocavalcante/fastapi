"""create users, brands, cars

Revision ID: 10bba3f265b1
Revises: 2fb7ca506706
Create Date: 2026-03-31 22:46:02.806773

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '10bba3f265b1'
down_revision: Union[str, Sequence[str], None] = '2fb7ca506706'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
