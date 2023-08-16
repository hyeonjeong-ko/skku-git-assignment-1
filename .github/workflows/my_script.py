import os

# Get the mapped owner value from the workflow's outputs
mapped_owner = os.environ['MAPPED_OWNER']

print("Mapped Owner:", mapped_owner)
