NODE_PACKAGE_MANAGER_CMD ?= npm

# Import helpers Makefile
-include ../helpers.mk

.PHONY: all
all: ## Execute all required commands to setup and validate
	@$(call inf, "Building and validating ephemeral-env-action using Node...")
	@$(NODE_PACKAGE_MANAGER_CMD) install
	@$(NODE_PACKAGE_MANAGER_CMD) run all

.PHONY: clean
clean: ## Deletes Node modules and generated packages
	@rm -rf node_modules/ lib/

#######################################
## Npde Targets
#######################################

.PHONY: npm/build
npm/build: ## Builds the action and generates the distribution ready to use
	@$(NODE_PACKAGE_MANAGER_CMD) run build

.PHONY: npm/lint
npm/lint: ## Runs linter using "eslint"
	@$(NODE_PACKAGE_MANAGER_CMD) run lint
