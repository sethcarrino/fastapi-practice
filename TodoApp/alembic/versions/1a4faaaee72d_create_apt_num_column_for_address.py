"""create apt_num column for address

Revision ID: 1a4faaaee72d
Revises: 7d4c8cec93cf
Create Date: 2023-05-15 21:48:35.969697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a4faaaee72d'
down_revision = '7d4c8cec93cf'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('address', sa.Column(
        'apt_num', sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column('address', 'apt_num')
