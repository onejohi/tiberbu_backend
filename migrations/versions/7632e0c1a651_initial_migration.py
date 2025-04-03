"""Initial migration

Revision ID: 7632e0c1a651
Revises: 
Create Date: 2025-04-03 04:25:40.299898

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7632e0c1a651'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('doctors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('specialty', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_doctors_first_name'), 'doctors', ['first_name'], unique=False)
    op.create_index(op.f('ix_doctors_id'), 'doctors', ['id'], unique=False)
    op.create_index(op.f('ix_doctors_last_name'), 'doctors', ['last_name'], unique=False)
    op.create_index(op.f('ix_doctors_specialty'), 'doctors', ['specialty'], unique=False)
    op.create_table('patients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('date_of_birth', sa.Date(), nullable=True),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('insurance_number', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('insurance_number'),
    sa.UniqueConstraint('phone_number')
    )
    op.create_index(op.f('ix_patients_first_name'), 'patients', ['first_name'], unique=False)
    op.create_index(op.f('ix_patients_id'), 'patients', ['id'], unique=False)
    op.create_index(op.f('ix_patients_last_name'), 'patients', ['last_name'], unique=False)
    op.create_table('permissions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_permissions_id'), 'permissions', ['id'], unique=False)
    op.create_index(op.f('ix_permissions_name'), 'permissions', ['name'], unique=True)
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_roles_id'), 'roles', ['id'], unique=False)
    op.create_index(op.f('ix_roles_name'), 'roles', ['name'], unique=True)
    op.create_table('appointments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=True),
    sa.Column('doctor_id', sa.Integer(), nullable=True),
    sa.Column('scheduled_at', sa.DateTime(), nullable=True),
    sa.Column('status', sa.Enum('scheduled', 'completed', 'canceled', name='appointment_status_enum'), nullable=True),
    sa.ForeignKeyConstraint(['doctor_id'], ['doctors.id'], ),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_appointments_id'), 'appointments', ['id'], unique=False)
    op.create_table('doctor_availability',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('doctor_id', sa.Integer(), nullable=True),
    sa.Column('available_from', sa.DateTime(), nullable=True),
    sa.Column('available_to', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['doctor_id'], ['doctors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_doctor_availability_id'), 'doctor_availability', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('user_permissions',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('permission_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['permission_id'], ['permissions.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'permission_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_permissions')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_doctor_availability_id'), table_name='doctor_availability')
    op.drop_table('doctor_availability')
    op.drop_index(op.f('ix_appointments_id'), table_name='appointments')
    op.drop_table('appointments')
    op.drop_index(op.f('ix_roles_name'), table_name='roles')
    op.drop_index(op.f('ix_roles_id'), table_name='roles')
    op.drop_table('roles')
    op.drop_index(op.f('ix_permissions_name'), table_name='permissions')
    op.drop_index(op.f('ix_permissions_id'), table_name='permissions')
    op.drop_table('permissions')
    op.drop_index(op.f('ix_patients_last_name'), table_name='patients')
    op.drop_index(op.f('ix_patients_id'), table_name='patients')
    op.drop_index(op.f('ix_patients_first_name'), table_name='patients')
    op.drop_table('patients')
    op.drop_index(op.f('ix_doctors_specialty'), table_name='doctors')
    op.drop_index(op.f('ix_doctors_last_name'), table_name='doctors')
    op.drop_index(op.f('ix_doctors_id'), table_name='doctors')
    op.drop_index(op.f('ix_doctors_first_name'), table_name='doctors')
    op.drop_table('doctors')
    # ### end Alembic commands ###
