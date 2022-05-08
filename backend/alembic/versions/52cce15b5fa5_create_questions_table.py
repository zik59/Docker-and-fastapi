"""create questions table

Revision ID: 52cce15b5fa5
Revises: 
Create Date: 2022-05-08 23:49:44.153753

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52cce15b5fa5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'questions',
        sa.Column('ID', sa.Integer, primary_key=True),
        sa.Column('id', sa.Integer),
        sa.Column('answer', sa.String(500), nullable=False),
        sa.Column('question', sa.String(500)),
        sa.Column('date', sa.Date)
    )

def downgrade():
    op.drop_table('questions')
