"""added the relationship between user and vedonr customer

Revision ID: 402801d4020f
Revises: 79b8f5bb0b72
Create Date: 2023-10-04 01:37:13.484240

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '402801d4020f'
down_revision = '79b8f5bb0b72'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('customer', schema=None) as batch_op:
        batch_op.create_foreign_key(batch_op.f('fk_customer_user_id_users'), 'users', ['user_id'], ['id'])

    with op.batch_alter_table('vendor', schema=None) as batch_op:
        batch_op.create_foreign_key(batch_op.f('fk_vendor_user_id_users'), 'users', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vendor', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_vendor_user_id_users'), type_='foreignkey')

    with op.batch_alter_table('customer', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_customer_user_id_users'), type_='foreignkey')

    # ### end Alembic commands ###
