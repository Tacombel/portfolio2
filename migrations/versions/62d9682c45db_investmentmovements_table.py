"""InvestmentMovements table

Revision ID: 62d9682c45db
Revises: 94fe22e29d3b
Create Date: 2018-06-22 12:52:49.834238

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62d9682c45db'
down_revision = '94fe22e29d3b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('investment_movements',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fecha', sa.DateTime(), nullable=True),
    sa.Column('cantidad', sa.Float(), nullable=True),
    sa.Column('cuenta', sa.String(length=10), nullable=True),
    sa.Column('comments', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('investment_movements')
    # ### end Alembic commands ###
