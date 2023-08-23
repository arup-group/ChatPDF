# Development Guide

## Dependencies

*`list all the dependencies that the code base and your local development environment requires to develop locally`*

E.g

- `nodejs 14`
- `npm`
- `docker`

## Local Development

*`list all the steps and commands to build the code in your locally environment`*

E.g.

```
npm run start
Visit http://localhost:3000
```

## Local Development (Docker)

*`list all the steps and commands to build the code as a docker image and container locally`*

E.g.

To build the docker image and container locally for development purposes follow the steps below

`<project>` = replace the tags with the desired information. e.g myprojectname-app

1. Build the docker image

```
docker build -t <project>:local .
```
2. Provision and run the docker container 

```
docker run --rm --name <project> -d -p 3000:80 <project>:local
```

3. Stop the docker container running 

```
docker stop <project>
```

4. Remove the docker container

```
docker rm <project>
```

5. Remove the docker image

```
docker rmi <project>
```

To view the application running in the docker container locally, browse to the application on http://localhost:3000 