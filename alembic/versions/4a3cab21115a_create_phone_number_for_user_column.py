"""Create phone number for user column

Revision ID: 4a3cab21115a
Revises: 
Create Date: 2026-01-12 19:10:03.811490

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4a3cab21115a'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String()))

def downgrade() -> None:
    op.drop_column('users', 'phone_number')
