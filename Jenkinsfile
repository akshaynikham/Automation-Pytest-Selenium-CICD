pipeline{
    agent {
        docker {
            image 'python:3.9' // use the python docker image.
            args '-v /dev/shm:/dev/shm'
        }
    }
    environment {
        PYTHON_ENV = 'pytest.env'
    }
    stages {
        stage('clone repository'){
            steps{
            git 'https://github.com/akshaynikham/Automation-Pytest-Selenium-CICD.git'
            }
        }
        stage('Install dependencies'){
             steps{
            sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests'){
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