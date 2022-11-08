---
date created: Monday, November 7th 2022, 6:10:56 pm
date modified: Tuesday, November 8th 2022, 5:27:06 pm
date_created: Monday, November 7th 2022, 6:10:56 pm
date_modified: Tuesday, November 8th 2022, 5:30:19 pm
---
## Commands
```shell

# spin up all containers with build flag and local yaml file 
docker-compose up --build -f ./docker-compose.dev.yml

# kill all containers
sudo docker kill $(sudo docker ps -q)

```