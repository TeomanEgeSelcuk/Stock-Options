import subprocess  # Importing the `subprocess` module for running shell commands
from pathlib import Path  # Importing the `Path` class from the `pathlib` module for working with file paths

def start_container_from_compose(compose_file):
    try:
        # Running the `docker-compose` command to start containers in detached mode (-d flag)
        # subprocess.run(["docker-compose", "-f", compose_file, "up"], check=True)
        # Use the -d option below for detached mode 
        subprocess.run(["docker-compose", "-f", compose_file, "up", "-d"], check=True)
        print(f"Containers started successfully using Docker Compose: {compose_file}")
    except subprocess.CalledProcessError as e:
        # Handling any errors that occur during the process
        print(f"An error occurred while starting the containers using Docker Compose: {e}")

def stop_and_remove_container_from_compose(compose_file):
    try:
        # Listing the images used by the created containers using `docker-compose images` command
        images = subprocess.check_output(["docker-compose", "-f", compose_file, "images", "-q"]).decode().splitlines()

        # Stopping the containers using `docker-compose down` command
        subprocess.run(["docker-compose", "-f", compose_file, "down"], check=True)
        print(f"Containers stopped and removed successfully using Docker Compose: {compose_file}")
        
        # Removing the Docker Compose services using `docker-compose rm` command
        subprocess.run(["docker-compose", "-f", compose_file, "rm", "-fsv"], check=True)
        print(f"Docker Compose services removed successfully: {compose_file}")

        # Removing the images using `docker image rm` command
        for image in images:
            subprocess.run(["docker", "image", "rm", image], check=True)

        print("Docker images deleted successfully")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while stopping or removing the containers using Docker Compose: {e}")

# Example usage
compose_file = Path("docker-compose.yml")  # Creating a `Path` object for the Docker Compose file path
start = 1 # Set to 1 to start the containers from Docker Compose

if start == 1:
    start_container_from_compose(compose_file)  # Calling the function to start the containers
else:
    stop_and_remove_container_from_compose(compose_file)  # Calling the function to stop and remove the containers
