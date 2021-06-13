docker build -f Dockerfile.development -t moviedb:latest . \
--build-arg SECRET_KEY="secretkey" \
--build-arg OMDB_API_KEY=""