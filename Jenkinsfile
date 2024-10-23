pipeline {
    agent {
        docker {
            image 'python:3.9'  // Use Python Docker image
        }
    }
    stages {
        stage('Clone Repository') {
            steps {
                // Cloning the repository that contains the automation code
                git 'https://github.com/akshaynikham/Automation-Pytest-Selenium-CICD.git'
            }
        }
        stage('create virtual environment') {
            steps {
               // creating virtual environment
                sh '''
                python -m venv venv
                . venv/bin/activate
                '''
            }
        }
        stage('Install Dependencies') {
            steps {
                // Installing dependencies listed in requirements.txt
                sh 'pip install --user -r requirements.txt'
            }
        }
        stage('Run Automation Tests') {
            steps {
                // Running the tests using pytest
                sh 'pytest --maxfail=5 --disable-warnings'
            }
        }
    }
    post {
        always {
            // Archiving test reports
            archiveArtifacts artifacts: '**/reports/*.html', allowEmptyArchive: true
            junit '**/reports/*.xml'
        }
    }
}
