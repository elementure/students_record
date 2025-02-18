pipeline {
    agent any

    environment {
        IMAGE_NAME = "fastapi_app"
        CONTAINER_NAME = "fastapi_container"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'git@github.com:elementure/students_record.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Deploy on EC2') {
            steps {
                sh '''
                docker stop $CONTAINER_NAME || true
                docker rm $CONTAINER_NAME || true
                docker run -d --name $CONTAINER_NAME --env-file /opt/fastapi_app/.env -p 80:8000 $IMAGE_NAME
                '''
            }
        }
    }
}
