# Docker Compose Setup: Jupyter Notebook & PostgreSQL

This Docker Compose configuration allows you to easily set up a containerized environment with Jupyter Notebook and PostgreSQL.

## Prerequisites

Before you begin, ensure you have Docker and Docker Compose installed on your system.

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/docker-jupyter-postgresql.git
   ```

2. Navigate to the project directory:

   ```bash
   cd docker-jupyter-postgresql
   ```

3. Start the Docker Compose environment:

   ```bash
   docker-compose up -d
   ```

   This command will create and start two containers: one for Jupyter Notebook and one for PostgreSQL.

4. Access Jupyter Notebook:

   - Open your web browser and navigate to [http://localhost:8888](http://localhost:8888).
   - You'll be prompted for a token. You can find the token in the terminal where you started the Docker Compose environment.

5. Access PostgreSQL:

   - You can connect to the PostgreSQL database using your preferred PostgreSQL client with the following details:
     - Host: `localhost` (or the IP address of your Docker host if you're using Docker Toolbox)
     - Port: `5432`
     - Username: `postgres`
     - Password: `password` (as set in the `docker-compose.yml` file)
     - Database: `mydb` (or the database name you specified in the `docker-compose.yml` file)

   - Alternatively, you can access PostgreSQL from the command line using `docker exec`. For example:

     ```bash
     docker exec -it your_postgres_container_name psql -U postgres
     ```

     Replace `your_postgres_container_name` with the actual name of your PostgreSQL container.

## Stopping and Cleanup

To stop the Docker Compose environment and remove containers, use the following command:

```bash
docker-compose down
```

## Customization

- You can customize the environment settings by modifying the `docker-compose.yml` file.
- To change the PostgreSQL database password, update the `POSTGRES_PASSWORD` environment variable in the `docker-compose.yml` file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
