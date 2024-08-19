pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/dredavidOps/devops_project.git'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: "${env.REPO_URL}"
            }
        }

        stage('Run db_connector.py') {
            steps {
                sh 'python db_connector.py'
            }
        }

        stage('Run rest_app.py') {
            steps {
                sh 'python rest_app.py'
            }
        }

        stage('Run web_app.py') {
            steps {
                sh 'python web_app.py'
            }
        }

        stage('Run Frontend Testing') {
            steps {
                sh 'python frontend_testing.py'
            }
        }

        stage('Run Backend Testing') {
            steps {
                sh 'python backend_testing.py'
            }
        }

        stage('Run Combined Testing') {
            steps {
                sh 'python combined_testing.py'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
