"""Initial migration

Revision ID: 7c0db7487d82
Revises: 
Create Date: 2025-06-29 00:06:05.256313

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c0db7487d82'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('lab_result', schema=None) as batch_op:
        batch_op.add_column(sa.Column('doctor_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('test_description', sa.Text(), nullable=True))
        batch_op.create_foreign_key(None, 'user', ['doctor_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('lab_result', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('test_description')
        batch_op.drop_column('doctor_id')

    # ### end Alembic commands ###
