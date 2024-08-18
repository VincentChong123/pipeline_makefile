import sys
import nbformat

# Read the notebook from stdin
notebook = nbformat.read(sys.stdin, as_version=4)

# Clear outputs from each cell
for cell in notebook.cells:
    cell.outputs = []

# Write the modified notebook to stdout
nbformat.write(notebook, sys.stdout, version=4)
