.PHONY: lint requester consumer log_processor log_backup test

setup:
	@pip install -r requirements_dev.txt
	@pip install -r requirements.txt

lint:
	@autopep8 -a --in-place --recursive *.py

consumer:
	@python consumer.py

log_processor:
	@python log_processor.py

log_backup:
	@bash log_backup.sh >> Backup.log

requester:
	@python requester.py

test:
	@nosetests --with-coverage -s --cover-erase --cover-package=controller