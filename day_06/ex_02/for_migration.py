def upgrade():
    op.create_table(
        'shipdata',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('alignment', sa.String(length=15), nullable=False),
        sa.Column('name', sa.String(length=15), nullable=False, unique=True),
        sa.Column('ship_class', sa.String(length=15), nullable=False),
        sa.Column('size', sa.Integer(), nullable=False),
        sa.Column('armed', sa.Boolean(), nullable=False),
        sa.Column('status', sa.String(length=10), nullable=False),
    )

    op.create_table(
        'crewdata',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('firstname', sa.String(length=15), nullable=False),
        sa.Column('lastname', sa.String(length=15), nullable=False),
        sa.Column('rank', sa.String(length=15), nullable=False),
        sa.Column('shipname', sa.String(length=15), sa.ForeignKey('shipdata.name'), nullable=False)
    )


def downgrade():
    op.drop_table('shipdata')
    op.drop_table('crewdata')