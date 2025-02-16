"""add foreign key to Review

Revision ID: 849a011656c8
Revises: c708d8f4894a
Create Date: 2025-02-14 02:14:24.808663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '849a011656c8'
down_revision = 'c708d8f4894a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('employee_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_reviews_employee_id_employees'), 'reviews', 'employees', ['employee_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_reviews_employee_id_employees'), 'reviews', type_='foreignkey')
    op.drop_column('reviews', 'employee_id')
    # ### end Alembic commands ###
