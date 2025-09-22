up:
	cd backend && docker build -t gh-workflow-backend . && docker run -p 8000:8000 gh-workflow-backend
