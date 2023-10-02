"""added one-to-many a relationship between the vendor and products

Revision ID: 8856bc2c0bfe
Revises: 7c4ac8b35b45
Create Date: 2023-10-02 22:57:39.721189

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8856bc2c0bfe'
down_revision = '7c4ac8b35b45'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('vendor_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_product_vendor_id_vendor'), 'vendor', ['vendor_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_product_vendor_id_vendor'), type_='foreignkey')
        batch_op.drop_column('vendor_id')

    # ### end Alembic commands ###