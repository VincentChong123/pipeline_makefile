pip install -q nbformat nbconvert

input_notebook_path=$1
backup_notebook_path=$input_notebook_path.ori.ipynb
echo backup $input_notebook_path to $input_notebook_path.ori.ipynb 
cp -f $input_notebook_path $backup_notebook_path
echo complete backup

python /home/vin/01-prj/tfip_da/public/pipeline_makefile/utils/clear-notebook-output-cells.py < $input_notebook_path > $input_notebook_path.clear-output.ipynb

jupyter nbconvert --to notebook --execute $input_notebook_path.clear-output.ipynb --output $input_notebook_path.executed.ipynb

cp -f $input_notebook_path.executed.ipynb $input_notebook_path