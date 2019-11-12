.PHONY: setup lint test requester consumer main log_backup user_data

setup:
	@pip install -r requirements_dev.txt
	@pip install -r requirements.txt

lint:
	@autopep8 -a --in-place --recursive *.py

test:
	@nosetests --with-coverage -s --cover-erase --cover-package=controller --cover-package=database --cover-package=mape

# runners

consumer:
	@python consumer.py

main:
	@python main.py

log_backup:
	@bash log_backup.sh >> Backup.log

user_data:
	@python user_data.py

requester:
	@python requester.py