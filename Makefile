IMAGE_NAME=gh-workflow-backend
CONTAINER_NAME=gh-workflow-backend

up: lint
	cd backend && docker build -t $(IMAGE_NAME) .
	docker run --rm -it -p 8000:8000 --name $(CONTAINER_NAME) $(IMAGE_NAME)

lint:
	cd backend && docker build --target lint -t $(IMAGE_NAME)-lint .
