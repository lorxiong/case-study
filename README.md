# case-study

Pre-reqs:
python3.6+
docker
docker-compose
virtualenv
pip

Setup virtualenv
```sh
virtualenv -p python3 env
source env/bin/activate
```

Install requirement packages
```sh
pip install -r requirements.txt
```

Build docker images and startup app and mongodb using docker-compose
```sh
docker-compose build
docker-compose up -d
docker-compose ps
```

Load data into mongodb
```sh
cd scripts && python insert_data.py
```

web browser
```sh
http://0.0.0.0:5000/
```

Shutdown containers and clean up
```sh
docker-compose down
docker system prune -a
```
