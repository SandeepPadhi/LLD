
project_name="carsystem"

mkdir -p $project_name/{models,dao,services,routes,configs,tests,scripts,docs} \
&& touch $project_name/{main.py,configs/config.yaml} \
&& touch $project_name/models/{__init__.py,user.py} \
&& touch $project_name/dao/{__init__.py,user_dao.py} \
&& touch $project_name/services/{__init__.py,user_service.py} \
&& touch $project_name/routes/{__init__.py,user_routes.py} \
&& touch $project_name/tests/{__init__.py,test_user.py} \
&& touch $project_name/scripts/{run.py,start.sh,deploy.sh} \
&& touch $project_name/docs/{README.md,API_DOCS.md} \
&& touch $project_name/.gitignore \
&& touch $project_name/requirements.txt \
&& touch $project_name/setup.py \
&& touch $project_name/pyproject.toml \
&& touch $project_name/Dockerfile \
&& touch $project_name/Makefile \
&& touch $project_name/.pre-commit-config.yaml