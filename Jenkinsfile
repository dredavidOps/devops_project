pipeline {
    agent any

    stages {
        stage('Pull from GitHub') {
            steps {
                // Pull code from the GitHub repository
                git branch: 'main', url: 'https://github.com/dredavidOps/devops_project.git'
            }
        }

        stage('Run Backend - rest_app.py') {
            steps {
                // Run the backend application
                sh 'nohup python rest_app.py &'
            }
        }

        stage('Run Backend Testing') {
            steps {
                // Run backend testing
                sh 'python backend_testing.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build Docker image locally
                sh 'docker build -t drewizzly/flask_api:latest .'
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                // Log in to Docker Hub and push the Docker image
                withCredentials([usernamePassword(credentialsId: 'DockerHub_Cred', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'echo "$DOCKER_PASSWORD" | docker login -u drewizzly --password-stdin'
                }
                sh 'docker push drewizzly/devops_project:latest'
            }
        }

        stage('Set Compose Image Version') {
            steps {
                // Update the version inside the .env file for Docker Compose
                script {
                    def version = sh(script: "docker images drewizzly/flask_api --format '{{.Tag}}'", returnStdout: true).trim()
                    sh "sed -i 's/IMAGE_VERSION=.*/IMAGE_VERSION=${version}/' .env"
                }
            }
        }

        stage('Clean Environment') {
            steps {
                // Run cleanup script
                sh 'python clean_environment.py'
            }
        }
    }

    post {
        always {
            // Clean up any remaining resources or background processes
            sh 'pkill -f rest_app.py || true'
            cleanWs()
        }
    }
}
