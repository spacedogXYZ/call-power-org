""" add campaign_type and campaign_subtype fields

Revision ID: 36c68d24bd98
Revises: 3a64ac078961
Create Date: 2015-06-11 13:06:02.119709

"""

# revision identifiers, used by Alembic.
revision = '36c68d24bd98'
down_revision = '3a64ac078961'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('campaign_campaign', schema=None) as batch_op:
        batch_op.add_column(sa.Column('campaign_subtype', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('campaign_type', sa.String(length=100), nullable=True))

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('campaign_campaign', schema=None) as batch_op:
        batch_op.drop_column('campaign_type')
        batch_op.drop_column('campaign_subtype')

    ### end Alembic commands ###
