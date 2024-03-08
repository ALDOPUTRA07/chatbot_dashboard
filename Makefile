##@ Clean-up
clean: ## remove output files from pytest & coverage
	@find . | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf
	@find . | grep -E ".ipynb_checkpoints" | xargs rm -rf