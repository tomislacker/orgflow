"""Add relationship before team-and-user

Revision ID: 2202b8ff11
Revises: 
Create Date: 2015-10-21 20:51:22.588320

"""

# revision identifiers, used by Alembic.
revision = '2202b8ff11'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'team_user_link',
        sa.Column(
            'team_id', sa.INTEGER(unsigned=True),
            sa.ForeignKey('team.id'), primary_key=True
        ),
        sa.Column(
            'user_id', sa.INTEGER(unsigned=True),
            sa.ForeignKey('user.id'), primary_key=True
        )
    )


def downgrade():
    op.drop_table('team_user_link')
