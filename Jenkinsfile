pipeline {
    agent any

    environment {
        REPO_URL = 'https://your-repo-url.git'
    }

    stages {
        stage('Pull Code from GitHub') {
            steps {
                git branch: 'main', url: "${env.REPO_URL}"
            }
        }

        stage('Run Backend (rest_app.py)') {
            steps {
                sh 'nohup python rest_app.py &'
            }
        }

        stage('Run Frontend (web_app.py)') {
            steps {
                sh 'nohup python web_app.py &'
            }
        }

        stage('Run Backend Testing (backend_testing.py)') {
            steps {
                sh 'python backend_testing.py'
            }
        }

        stage('Run Frontend Testing (frontend_testing.py)') {
            steps {
                sh 'python frontend_testing.py'
            }
        }

        stage('Run Combined Testing (combined_testing.py)') {
            steps {
                sh 'python combined_testing.py'
            }
        }

        stage('Clean Environment (clean_environment.py)') {
            steps {
                sh 'python clean_environment.py'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
