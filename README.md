## Stock price API

This project is a lightweight interface for a public API [finnhub.io](https://finnhub.io).

Its purpose is to serve an IoT application developed for [micro:bit](https://microbit.org) that triggers an alarm when a stock price goes below or above a set threshold.

### Usage

#### Create new AWS Docker Machine

```bash
docker-machine create --driver amazonec2 --amazonec2-region eu-west-2 --amazonec2-open-port 8080 --amazonec2-open-port 8888 --amazonec2-open-port 2377 --amazonec2-open-port 80 --amazonec2-open-port 443 --amazonec2-open-port 5000 --amazonec2-access-key <YOUR_ACCESS_KEY> --amazonec2-secret-key <YOUR_SECRET_KEY>
```

#### SSH to your new created instance

```bash
docker-machine ssh aws-stock-price-api
```

#### Clone this project

```bash
git clone -b deploy-dev-v1 https://github.com/rosudavidg/stock-price-api.git
```

#### Change directory to project's root

```bash
cd stock-price-api
```


#### Create secret files

```bash
mkdir secrets

echo "YOUR_SECRET_BEARER_TOKEN" > secrets/bearer_token
echo "YOUR_SECRET_FINNHUB_API" > secrets/finnhub_api_token
```

#### Create a Docker Swarm

```bash
sudo docker swarm init
```

#### Deploy application

```bash
sudo docker stack deploy -c docker-compose.yml stock-price-api
```

#### Remove application

```bash
docker stack rm stock-price-api
```
