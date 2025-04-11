"""Update database schemas

Revision ID: 7b65501be08c
Revises: 06e49731a108
Create Date: 2025-04-11 23:12:49.284419

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7b65501be08c'
down_revision: Union[str, None] = '06e49731a108'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('appointments', sa.Column('start_time', sa.DateTime(), nullable=False))
    op.add_column('appointments', sa.Column('end_time', sa.DateTime(), nullable=False))
    op.add_column('doctors', sa.Column('user_id', sa.Integer(), nullable=True))
    op.add_column('doctors', sa.Column('is_active', sa.Boolean(), nullable=True))
    op.create_foreign_key(None, 'doctors', 'users', ['user_id'], ['id'])
    op.add_column('patients', sa.Column('insurance_provider', sa.String(), nullable=True))
    op.add_column('patients', sa.Column('identification_number', sa.String(), nullable=True))
    op.create_unique_constraint(None, 'patients', ['identification_number'])
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_constraint(None, 'patients', type_='unique')
    op.drop_column('patients', 'identification_number')
    op.drop_column('patients', 'insurance_provider')
    op.drop_constraint(None, 'doctors', type_='foreignkey')
    op.drop_column('doctors', 'is_active')
    op.drop_column('doctors', 'user_id')
    op.drop_column('appointments', 'end_time')
    op.drop_column('appointments', 'start_time')
    # ### end Alembic commands ###
