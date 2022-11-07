## Commands
```shell

# spin up all containers with build flag and local yaml file 
docker-compose up --build -f ./docker-compose.dev.yml

# kill all containers
sudo docker kill $(sudo docker ps -q)

```