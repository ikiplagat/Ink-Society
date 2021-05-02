"""Initial Migration

Revision ID: 5f0ad0ce2523
Revises: 9323527d9c8d
Create Date: 2021-05-02 11:35:11.579299

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f0ad0ce2523'
down_revision = '9323527d9c8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'date')
    # ### end Alembic commands ###