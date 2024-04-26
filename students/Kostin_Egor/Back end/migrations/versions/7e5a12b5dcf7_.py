"""empty message

Revision ID: 7e5a12b5dcf7
Revises: 4f4cdb755fb2
Create Date: 2024-04-24 20:52:22.792600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e5a12b5dcf7'
down_revision = '4f4cdb755fb2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('AplSer',
    sa.Column('application_id', sa.Integer(), nullable=False),
    sa.Column('service_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['application_id'], ['application.id_application'], ),
    sa.ForeignKeyConstraint(['service_id'], ['service.id_service'], ),
    sa.PrimaryKeyConstraint('application_id', 'service_id')
    )
    op.add_column('application', sa.Column('is_active', sa.Boolean(), nullable=True))
    op.drop_constraint('application_id_service_fkey', 'application', type_='foreignkey')
    op.drop_column('application', 'id_service')
    op.add_column('service', sa.Column('is_active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('service', 'is_active')
    op.add_column('application', sa.Column('id_service', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('application_id_service_fkey', 'application', 'service', ['id_service'], ['id_service'])
    op.drop_column('application', 'is_active')
    op.drop_table('AplSer')
    # ### end Alembic commands ###
