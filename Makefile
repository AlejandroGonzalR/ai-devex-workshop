SUBDIRS := scaffolding-cli observability-stack ephemeral-env-action

-include helpers.mk

#######################################
## Macros
#######################################

# Run a target in all subdirectories
define run_in_subdirs
	@for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir $(1); \
	done
endef

#######################################
## Run targets
#######################################

.PHONY: run/all
run/all: ## Run "all" target in all subdirectories
	$(call run_in_subdirs,all)

.PHONY: run/%
run/%: ## Run "all" target in a specific subdirectory (e.g. make run/scaffolding-cli)
	@$(MAKE) -C $* all

#######################################
## Clean targets
#######################################

.PHONY: clean
clean: ## Clean all subdirectories
	$(call run_in_subdirs,clean)

.PHONY: clean/%
clean/%: ## Clean a specific subdirectory (e.g. make clean/scaffolding-cli)
	@$(MAKE) -C $* clean
