# 1. Cleanup
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
docker system prune -a -f

# 2. Build
docker build -t students-api .

# 3. Run
docker run -d -p 8000:8000 --name students-container students-api

# 4. Check
docker ps
