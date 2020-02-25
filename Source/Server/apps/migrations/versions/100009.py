"""0009 - Base

Revision ID: 100009
Revises: 100008
Create Date: 2020-02-13

"""

# revision identifiers, used by Alembic.
revision = '100009'
down_revision = '100008'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql


def upgrade():
	### commands auto generated by Alembic - please adjust! ###

	### end Alembic commands ###
	u_qstr1 = "ALTER TABLE `mp_clients` ADD COLUMN `depEnrolled` text NULL AFTER `hasPausedPatching`;"
	op.execute(u_qstr1)

	u_qstr2 = "ALTER TABLE `mp_clients` ADD COLUMN `mdmEnrolled` text NULL AFTER `depEnrolled`;"
	op.execute(u_qstr2)

	u_qstr3="ALTER TABLE `mp_software` ADD COLUMN `sw_app_path` text NULL AFTER `sReboot`;"
	op.execute(u_qstr3)


def downgrade():
	### commands auto generated by Alembic - please adjust! ###

	### end Alembic commands ###
	d_qstr1 = "ALTER TABLE `mp_software` DROP COLUMN `sw_app_path`;"
	op.execute(d_qstr1)

	d_qstr1 = "ALTER TABLE `mp_clients` DROP COLUMN `depEnrolled`;"
	op.execute(d_qstr1)

	d_qstr1 = "ALTER TABLE `mp_clients` DROP COLUMN `mdmEnrolled`;"
	op.execute(d_qstr1)

