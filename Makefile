.PHONY: all check-version docker-build docker-push docker-run run set-revision clean setup
VERSION := $(strip $(shell [ -d .git ] && git describe --always --tags --dirty))
BUILD_DATE := $(shell date -u +"%Y-%m-%dT%H:%M:%S%Z")
VCS_URL := $(shell [ -d .git ] && git config --get remote.origin.url)
VCS_REF := $(strip $(shell [ -d .git ] && git rev-parse --short HEAD))
# IS_TAG := $(shell [ -d .git ] && git describe --exact-match HEAD || echo 'no tags')
VCS_REF_MSG := $(shell if [ "$(IS_TAG)" != "" ]; then git tag -l -n1 $(IS_TAG) | awk '{$$1 = ""; print $$0;}'; else git log --format='%s' -n 1 $(VCS_REF); fi)

all: docker-build;

check-version:
	$(info $(VERSION))
ifneq (,$(findstring dirty,$(VERSION)))
	$(error Working copy dirty, aborting)
endif

docker-build:
	docker build \
		--build-arg BUILD_DATE="$(BUILD_DATE)" \
		--build-arg VERSION="$(VERSION)" \
		--build-arg VCS_URL="$(VCS_URL)" \
		--build-arg VCS_REF="$(VCS_REF)" \
		--build-arg VCS_REF_MSG="$(VCS_REF_MSG)" \
		--compress \
		-t salimane/flask-mvc:latest .

docker-push: #check-version
	if [ "$(IS_TAG)" != "" ]; then \
		docker tag salimane/flask-mvc:latest salimane/flask-mvc:$(VERSION);\
	fi
	docker push salimane/flask-mvc

docker-run:
	docker-compose up -d

run:
	python runserver.py

set-revision:
	echo $(BUILD_DATE) > BUILD_TIME
	if [ -d ".git" ]; then echo "$(VERSION)"; fi > BUILD_REVISION

clean:
	find . -name '*venv*' | xargs rm -rf
	rm -rf "htmlcov" ".cache" ".coverage"

setup:
	script/setup

test:
	script/test

flake:
	flake8 --config=setup.cfg --statistics --count .

autopep8:
	autopep8 -ira .
