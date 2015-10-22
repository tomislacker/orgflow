### Running a MySQL container

```sh
docker run \
    -it \
    --name orgflowmysql \
    -e "MYSQL_ROOT_PASSWORD=password" \
    -p 3306:3306 \
    mysql:5.6
```
