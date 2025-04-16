"""init

Revision ID: bfd67ad5eb06
Revises:
Create Date: 2025-04-15 13:02:29.045069

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'bfd67ad5eb06'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('weather_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('temperature', sa.Float(), nullable=False),
    sa.Column('humidity', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_weather_city_hash', 'weather_data', ['city'], unique=False, postgresql_using='hash')
    op.create_index(op.f('ix_weather_data_date'), 'weather_data', ['date'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_weather_data_date'), table_name='weather_data')
    op.drop_index('ix_weather_city_hash', table_name='weather_data', postgresql_using='hash')
    op.drop_table('weather_data')
    # ### end Alembic commands ###
