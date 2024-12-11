"""create t_users

Revision ID: ecdc8e0f4199
Revises: 
Create Date: 2024-12-10 14:46:00.386288

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ecdc8e0f4199'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "t_users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username", sa.String(50)),
        sa.Column("password", sa.String(50))
    )



def downgrade() -> None:
    op.drop_table("t_users")