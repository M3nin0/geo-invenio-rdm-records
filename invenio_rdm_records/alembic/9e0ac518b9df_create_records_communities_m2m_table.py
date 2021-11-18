# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
#
# Invenio-RDM-Records is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Create records/communities M2M table."""

import sqlalchemy as sa
from alembic import op
from sqlalchemy_utils import UUIDType

# revision identifiers, used by Alembic.
revision = '9e0ac518b9df'
down_revision = ('8ed1a438601c', '88d1463de5c0')
branch_labels = ()
depends_on = 'de9c14cbb0b2'


def upgrade():
    """Upgrade database."""
    op.create_table(
        'rdm_parents_community',
        sa.Column(
            'community_id',
            UUIDType(),
            nullable=False
        ),
        sa.Column(
            'record_id',
            UUIDType(),
            nullable=False
        ),
        sa.ForeignKeyConstraint(
            ['community_id'],
            ['communities_metadata.id'],
            name=op.f(
                'fk_rdm_parents_community_community_id_communities_metadata'),
            ondelete='CASCADE'
        ),
        sa.ForeignKeyConstraint(
            ['record_id'],
            ['rdm_parents_metadata.id'],
            name=op.f(
                'fk_rdm_parents_community_record_id_rdm_parents_metadata'),
            ondelete='CASCADE'
        ),
        sa.PrimaryKeyConstraint(
            'community_id',
            'record_id',
            name=op.f('pk_rdm_parents_community')
        )
    )


def downgrade():
    """Downgrade database."""
    op.drop_table('rdm_parents_community')