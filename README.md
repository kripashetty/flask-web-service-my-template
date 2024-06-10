# Developer Setup 

### Setup virtual environment and install dependencies

> python3 -m venv venv

> source venv/bin/activate

> pip install -r requirements.txt

# Run application locally as a docker image

### Prerequisites

Make sure you have the following installed on your machine:

- [Docker](https://www.docker.com/products/docker-desktop)

### Dockerizing the Application

Follow these steps to Dockerize and run the Flask application.

#### 1. Clone the Repository

Clone this repository to your local machine:
```sh
git clone https://github.com/kripashetty/flask-web-service-my-template.git
cd web-app
```

#### 2. Build the Docker image
```sh
docker build -t my-flask-api .
```

#### 3. Run the docker Container
```sh
docker run -d -p 5000:5000 my-flask-api
```


#### 4. Verify the application is running locally
Create a item record : 
```sh
curl --location 'http://127.0.0.1:5000/item/tea' \
--header 'Content-Type: application/json' \
--data '{
    "price":100
}'
```
Get all items : 
```sh
curl --location 'http://127.0.0.1:5000/items'
```

Get welcome message : 
```sh
curl --location 'http://127.0.0.1:5000/'
```