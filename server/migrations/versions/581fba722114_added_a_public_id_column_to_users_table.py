"""added a public id column to users table 

Revision ID: 581fba722114
Revises: 711a28c44606
Create Date: 2023-10-03 17:33:28.662397

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '581fba722114'
down_revision = '711a28c44606'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('public_id', sa.String(length=50), nullable=True))
        batch_op.create_unique_constraint('User_unique_constraint', ['public_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint('User_unique_constraint', type_='unique')
        batch_op.drop_column('public_id')

    # ### end Alembic commands ###
