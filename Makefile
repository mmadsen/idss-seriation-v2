SHELL := /bin/bash
.ONESHELL:
DIR := ${CURDIR}


# Use this target if you manually use virtualenv on OS X or a desktop development
# environment instead of an autoswitcher
.PHONY: setup-dev
setup-dev:
	( \
	rm -rf venv ; \
	virtualenv --clear --always-copy venv/idss_seriation_v2 ; \
	source venv/idss_seriation_v2/bin/activate ; \
	pip3 install -r requirements.txt ; \
	pip3 install -r requirements-dev.txt ; \
	pre-commit install ; \
	pip3 install -e . ; \
	pytest ; \
	)
	@echo " "
	@echo "If no errors appeared; type the following to use the virtual env:  source venv/asset_utilization_service/bin/activate"
	@echo " "

.PHONY: setup-ec2
setup-ec2:
	( \
	virtualenv --clear --always-copy venv/idss_seriation_v2 ; \
	source venv/idss_seriation_v2/bin/activate ; \
	pip3 --isolated --no-cache-dir install -r requirements.txt ; \
	pip3 --isolated --no-cache-dir install -r requirements-dev.txt ; \
	pip3 install -e . ; \
	)
	@echo " "
	@echo "If no errors appeared; type the following to use the virtual env:  source venv/asset_utilization_service/bin/activate"
	@echo " "

.PHONY: update-toc
update-toc:
	tools/gh-md-toc --insert --no-backup README.md

.PHONY: image
image:
	docker build . -t 'mmadsen/idss_seriation_v2' -f Dockerfile.service

.PHONY: cleanimage
cleanimage:
	docker build --no-cache . -t 'mmadsen/idss_seriation_v2' -f Dockerfile.service

.PHONY: tag
tag:
	docker tag mmadsen/idss_seriation_v2:latest mmadsen/idss_seriation_v2:$(TAG)
