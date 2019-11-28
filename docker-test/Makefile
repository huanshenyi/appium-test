.DEFAULT_GOAL := help
.PHONY: help

PROJECT_NAME=appium

################
## appium
################
appium-up: ## [appium] appiumスタート
	docker-compose up -d

iplist:
	@docker network inspect ${PROJECT_NAME}_default | jq -r '.[0].Containers[] | [.Name, "-->", .IPv4Address] | @csv' | column -t -s "," | xargs -ICONTAINER echo "- CONTAINER"
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

