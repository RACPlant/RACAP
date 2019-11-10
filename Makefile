.PHONY: setup lint test requester consumer log_processor log_backup user_data

setup:
	@pip install -r requirements_dev.txt
	@pip install -r requirements.txt

lint:
	@autopep8 -a --in-place --recursive *.py

test:
	@nosetests --with-coverage -s --cover-erase --cover-package=controller

# runners

consumer:
	@python consumer.py

log_processor:
	@python log_processor.py

log_backup:
	@bash log_backup.sh >> Backup.log

user_data:
	@python user_data.py

requester:
	@python requester.py