# Template for deploying ML models using Flask + Gunicorn + Nginx inside Docker

## Running the solution

In order to run this solution, you just have to install Docker, Docker compose, then clone this repository, and then:
```
run bash run_docker.sh
```

For Docker installation instructions follow:

— [Docker installation](https://medium.com/r/?url=https%3A%2F%2Fdocs.docker.com%2Fengine%2Finstall%2Fubuntu%2F)

— [Make Docker run without root](https://medium.com/r/?url=https%3A%2F%2Fdocs.docker.com%2Fengine%2Finstall%2Flinux-postinstall%2F)

— [Docker Compose installation](https://medium.com/r/?url=https%3A%2F%2Fdocs.docker.com%2Fcompose%2Finstall%2F)

## Understanding the solution

— The detailed way: check my Medium post regarding this solution.

— The fast way: the project is structured as follows: Flask app and WSGI entry point are localed in flask_app directory. Nginx and project configuration files are located in nginx directory. Both directories contain Docker files that are connected using docker_compose.yml file in the main directory. 
  
   For simplicity, I also added run_docker.sh file for an even easier setting-up and running this solution. 
```
.
├── flask_app 
│   ├── app.py          
│   ├── wsgi.py
│   └── Dockerfile
├── nginx
│   ├── nginx.conf          
│   ├── project.conf
│   └── Dockerfile
├── docker-compose.yml
└── run_docker.sh
```
