"""created_at should not be NULLable

Revision ID: 2d889f0751f
Revises: 2940488ae39
Create Date: 2015-10-21 21:30:22.786569

"""

# revision identifiers, used by Alembic.
revision = '2d889f0751f'
down_revision = '2940488ae39'
branch_labels = None
depends_on = None

from alembic import op
import datetime
from sqlalchemy.dialects import mysql


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('team', 'created_at',
                    existing_type=mysql.DATETIME(),
                    default=datetime.datetime.utcnow,
                    nullable=False)
    op.alter_column('team_user_link', 'created_at',
                    existing_type=mysql.DATETIME(),
                    default=datetime.datetime.utcnow,
                    nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('team_user_link', 'created_at',
                    existing_type=mysql.DATETIME(),
                    default=datetime.datetime.utcnow,
                    nullable=True)
    op.alter_column('team', 'created_at',
                    existing_type=mysql.DATETIME(),
                    default=datetime.datetime.utcnow,
                    nullable=True)
    ### end Alembic commands ###
