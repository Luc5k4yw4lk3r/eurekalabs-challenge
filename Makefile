RUN=docker-compose run --rm app

build:
	docker-compose build

run:
	docker-compose up

shell:
	docker exec -t -i eurekalabs-challenge_app_1 sh

stop:
	docker-compose down