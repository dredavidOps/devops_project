pipeline {
    agent any

    stages {
        stage('Pull from GitHub') {
            steps {
                git branch: 'main', url: 'https://github.com/dredavidOps/devops_project.git'
            }
        }

        stage('Run Backend - rest_app.py') {
            steps {
                sh 'nohup python rest_app.py &'
            }
        }

        stage('Run Backend Testing') {
            steps {
                sh 'python backend_testing.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t drewizzly/flask_api:latest .'
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'DockerHub_Cred', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'echo "$DOCKER_PASSWORD" | docker login -u drewizzly --password-stdin'
                }
                sh 'docker push drewizzly/flask_api:latest'
            }
        }

        stage('Run Docker Compose') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Clean Environment') {
            steps {
                sh 'python clean_environment.py'
            }
        }
    }

    post {
        always {
            sh 'pkill -f rest_app.py || true'
            cleanWs()
        }
    }
}