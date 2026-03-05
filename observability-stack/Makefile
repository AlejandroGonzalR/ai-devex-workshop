DOCKER_CMD ?= docker

# Import helpers Makefile
-include ../helpers.mk

.PHONY: all
all: ## Execute all required commands to setup and run
	@$(call inf, "Mounting observability stack \(Grafana/Prometheus\)...")
	@$(MAKE) docker/up

.PHONY: clean
clean:
	@$(MAKE) docker/down

#######################################
## Docker Compose Targets
#######################################

.PHONY: docker/up
docker/up: ## Mounts all compose containers
	@$(DOCKER_CMD) compose up --detach

.PHONY: docker/down
docker/down: ## Stops all compose containers
	@$(DOCKER_CMD) compose down
