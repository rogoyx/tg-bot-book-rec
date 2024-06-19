
docker volume create postgres_vol_1
docker volume create postgres_vol_2
docker volume create clickhouse_vol

docker network create app-net

#POSTGRES
docker run --rm -d \
  --name postgres_super \
  -e POSTGRES_PASSWORD=pass \
  -e POSTGRES_USER=admin \
  -e POSTGRES_DB=test_app \
  -v postgres_vol_1:/var/lib/postgresql/data \
  --net=app-net \
  postgres

docker run --rm -d \
  --name postgres_super \
  -e POSTGRES_PASSWORD=pass \
  -e POSTGRES_USER=admin \
  -e POSTGRES_DB=test_app \
  -v postgres_vol_1:/var/lib/postgresql/data \
  --net=app-net \
  -p 5432:5432 \
  postgres


docker exec -it postgres_super bash
psql -U admin test_app

docker ps # list of working containers


# SUPERSET
docker run -d --rm --net=app-net -p 80:8088 -e "SUPERSET_SECRET_KEY=rogoyx" --name superset apache/superset

# initilize local superset instance

docker exec -it superset superset fab create-admin \
              --username admin \
              --firstname Superset \
              --lastname Admin \
              --email admin@superset.com \
              --password admin

docker exec -it superset superset db upgrade

docker exec -it superset superset init

