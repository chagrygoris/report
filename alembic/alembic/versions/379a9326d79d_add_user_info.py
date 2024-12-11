"""add user info

Revision ID: 379a9326d79d
Revises: ecdc8e0f4199
Create Date: 2024-12-10 15:18:04.762694

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '379a9326d79d'
down_revision: Union[str, None] = 'ecdc8e0f4199'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    table = sa.sql.table(
        "t_users", 
        sa.sql.column("id", sa.Integer),
        sa.sql.column("username", sa.String(50)),
        sa.sql.column("password", sa.String(50))
    )
    op.bulk_insert(
        table,
        [
            {
                "id": 1,
                "username": "JustANickname",
                "password": "12345"
            },
            {
                "id": 2,
                "username": "StarGazer88",
                "password": "Moonlight!2023"
            },
            {
                "id": 3,
                "username": "BookLover91",
                "password": "ReadRelax2023"
            }
        ]
    )


def downgrade() -> None:
    op.execute('''DELETE FROM t_users''')
