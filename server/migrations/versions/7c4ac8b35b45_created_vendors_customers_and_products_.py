"""created vendors, customers and products tables 

Revision ID: 7c4ac8b35b45
Revises: 7a236c811b76
Create Date: 2023-10-02 20:29:26.733199

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c4ac8b35b45'
down_revision = '7a236c811b76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_customer')
    with op.batch_alter_table('customer', schema=None) as batch_op:
        batch_op.create_unique_constraint('Customer_unique_constraint', ['phone_number', 'email'])

    with op.batch_alter_table('vendor', schema=None) as batch_op:
        batch_op.add_column(sa.Column('company', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('phone_number', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('email', sa.String(), nullable=True))
        batch_op.create_unique_constraint('Vendor_unique_constraint', ['phone_number', 'email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vendor', schema=None) as batch_op:
        batch_op.drop_constraint('Vendor_unique_constraint', type_='unique')
        batch_op.drop_column('email')
        batch_op.drop_column('phone_number')
        batch_op.drop_column('company')

    with op.batch_alter_table('customer', schema=None) as batch_op:
        batch_op.drop_constraint('Customer_unique_constraint', type_='unique')

    op.create_table('_alembic_tmp_customer',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('phone_number', sa.INTEGER(), nullable=True),
    sa.Column('email', sa.VARCHAR(), nullable=True),
    sa.Column('joined', sa.DATETIME(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone_number'),
    sa.UniqueConstraint('phone_number', 'email', name='Customer_unique_constraint')
    )
    # ### end Alembic commands ###