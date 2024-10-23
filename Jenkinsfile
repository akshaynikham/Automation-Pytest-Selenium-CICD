pipeline {
    agent {
        docker {
            image 'python:3.9' 
            args '-v /dev/shm:/dev/shm' 
        }
    }
    environment {
        VIRTUAL_ENV = '.venv'
        PATH = ".venv/bin:$PATH"
    }
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/akshaynikham/Automation-Pytest-Selenium-CICD.git'
            }
        }
        stage('Set Up Virtual Environment') {
            steps {
                sh 'python -m venv $VIRTUAL_ENV' 
                sh 'pip install -U pip'           
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest --maxfail=5 --disable-warnings'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: '**/reports/*.html', allowEmptyArchive: true
            junit '**/reports/*.xml'
        }
    }
}
