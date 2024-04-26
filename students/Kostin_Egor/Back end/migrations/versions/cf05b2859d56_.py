"""empty message

Revision ID: cf05b2859d56
Revises: 7e5a12b5dcf7
Create Date: 2024-04-25 15:21:06.020317

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'cf05b2859d56'
down_revision = '7e5a12b5dcf7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('attachment', sa.Column('url', sa.String(), nullable=False))
    op.drop_column('attachment', 'file_name')
    op.drop_column('attachment', 'file_blob')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('attachment', sa.Column('file_blob', postgresql.BYTEA(), autoincrement=False, nullable=True))
    op.add_column('attachment', sa.Column('file_name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('attachment', 'url')
    # ### end Alembic commands ###
