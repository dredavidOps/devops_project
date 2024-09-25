import os
import requests

# Flask app stop requests
requests.get('http://127.0.0.1:5000/stop_server')
requests.get('http://127.0.0.1:5001/stop_server')

# Docker commands to bring down containers and remove local images
def clean_docker_environment():
    try:
        # Bring down the containers
        os.system('docker-compose down')

        # Remove local images
        os.system('docker rmi -f $(docker images -q)')
        print("Docker environment cleaned up successfully.")
    except Exception as e:
        print(f"Error cleaning Docker environment: {e}")

if __name__ == '__main__':
    clean_docker_environment()
