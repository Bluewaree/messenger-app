# messenger-app

```bash
# .env file needeed even if empty (All variables are set to default)

# run dockerized app
$ docker-compose up

# run asyncio unit test 
$ docker exec -it messenger-app_app_1 pytest -m "asyncio"

# default landing page
$ http://localhost:8000

```
