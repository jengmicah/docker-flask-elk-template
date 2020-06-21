## Ensure docker-machine is installed

- Documentation [here](https://docs.docker.com/machine/install-machine/#install-machine-directly)

## OPTIONAL: max_map_count to at least 262144edit

- `docker-machine create default --virtualbox-no-vtx-check test`
- `docker-machine ssh`
- `sudo sysctl -w vm.max_map_count=262144`

## Start Elasticsearch and Kibana

- `docker-compose up -d`
- `docker-compose logs -f elasticsearch`
- `docker-compose ps`#   d o c k e r - f l a s k - e l k - t e m p l a t e  
 