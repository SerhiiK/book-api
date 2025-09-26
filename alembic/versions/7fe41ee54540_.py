"""empty message

Revision ID: 7fe41ee54540
Revises: 
Create Date: 2024-12-14 15:02:47.620455

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

import os
import json


# revision identifiers, used by Alembic.
revision: str = '7fe41ee54540'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create the books table and seed it with the demo dataset."""
    book = op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('author', sa.String(), nullable=True),
    sa.Column('pages', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with open(os.path.join(os.path.dirname(__file__), "../data/books.json")) as f:
        book_data = f.read()

    op.bulk_insert(book, json.loads(book_data))


def downgrade() -> None:
    """Drop the books table created in :func:`upgrade`."""
    op.drop_table('books')
