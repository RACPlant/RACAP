.PHONY: lint
lint:
	@autopep8 -a --in-place --recursive *.py

.PHONY: run
run:
	@python main.py

.PHONY: run-consumer
run-consumer:
	@python consumer.py

.PHONY: test
test:
	@nosetests --with-coverage -s --cover-erase --cover-package=controller