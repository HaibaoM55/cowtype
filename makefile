# Makefile for Python application

PYTHON = python3
PIP = pip3
APP = main.py
APP_NAME = cowtype
INSTALL_DIR = /usr/local/bin
VENV = .venv
VENV_ACTIVATE = $(VENV)/bin/activate
.PHONY: all run install uninstall clean lint format test help
all: install
run:
	$(PYTHON) $(APP)
install:
	$(PIP) install -r requirements.txt --break-system-packages
	@echo '#!/bin/bash\n$(PYTHON) $(CURDIR)/$(APP) "$$@"' | sudo tee $(INSTALL_DIR)/$(APP_NAME) > /dev/null
	sudo chmod +x $(INSTALL_DIR)/$(APP_NAME)
	@echo "Installed! Run with: $(APP_NAME)"
uninstall:
	sudo rm -f $(INSTALL_DIR)/$(APP_NAME)
	@echo "Uninstalled $(APP_NAME)"
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .pytest_cache dist build
help:
	@echo "Available targets:"
	@grep -E '^##' Makefile | sed 's/## /  /'