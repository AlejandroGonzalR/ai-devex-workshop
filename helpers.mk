export OS ?= $(shell uname -s | tr '[:upper:]' '[:lower:]')

SHELL := /bin/bash

.DEFAULT_GOAL := help

#######################################
## Bash Colors
#######################################

RED = $(shell echo '\033[0;31m')
GREEN = $(shell echo '\033[0;32m')
BLUE = $(shell echo '\033[0;34m')
PURPLE = $(shell echo '\033[0;95m')
CYAN = $(shell echo '\033[0;36m')

# Reset color
NC = $(shell echo '\033[0m')

#######################################
## Macros
#######################################
inf = echo "$(PURPLE)=> $(1)$(NC)"

#######################################
## Self-documented Help
#######################################

.PHONY: help
help:
	@printf "\n$(PURPLE)Available targets:$(NC)\n"
	@$(MAKE) help/generate

## Display all available targets with description, this looks for a `##` after every target definition
.PHONY: help/generate
help/generate:
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | \
		awk \
		'BEGIN { \
			FS = ":.*?## " ; \
		}; \
		{ \
			printf "\tmake $(BLUE) %-15s $(NC) %s\n", $$1, $$2 \
		}'
