pipeline {
    agent any

    stages{
        stage('Checkout') {
            steps{
                echo 'Checking out the source code from Github...'
                Checkout scm
            }
        }

        stage('Build Docker Image'){
            steps {
                echo 'Building the Docker image for Flask API...'
                sh 'docker build -t flask-api .'
            }
        }

        stage('Run Docker Container') {
            steps {
                echo 'Running the Flask API container...'
                sh '''
                    docker rm -f flask-container || true
                    docker run -d -p 5000:5000 --name flask-container flask-api
                '''
            }
        }
    }
}