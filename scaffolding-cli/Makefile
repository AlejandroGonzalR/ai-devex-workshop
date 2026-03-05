DOCKER_CMD ?= docker
DOCKERFILE_PATH ?= Dockerfile

IMAGE_TAG ?= scaffolding-cli

# Import helpers Makefile
-include ../helpers.mk

.PHONY: all
all: ## Execute all required commands to setup and run
	@$(call inf, "Setupping scaffolding-cli...")
	@$(MAKE) docker/build
	@$(MAKE) docker/run
	@$(MAKE) docker/ms-help


.PHONY: clean
clean:
	@$(MAKE) docker/clean

#######################################
## Docker Targets
#######################################

.PHONY: docker/build
docker/build: ## Builds the CLI Docker image
	@$(DOCKER_CMD) build -f $(DOCKERFILE_PATH) -t $(IMAGE_TAG) .

.PHONY: docker/run
docker/run: ## Runs the CLI container by default
	$(DOCKER_CMD) run --rm $(IMAGE_TAG) $(CMD)

.PHONY: docker/ms-help
docker/ms-help: CMD=scaffold microservice --help ## Runs the CLI container with 'Microservice' command
docker/ms-help: docker/run

.PHONY: docker/clean
docker/clean: ## Cleans the workspace
	$(DOCKER_CMD) rmi $(IMAGE_TAG)
