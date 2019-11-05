.PHONY: lint
lint:
	@autopep8 -a --in-place --recursive *.py

.PHONY: run
run:
	@python main.py

.PHONY: run-consumer
run-consumer:
	@python consumer.py