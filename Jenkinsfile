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
        stage('Create Virtual Environment') {
            steps {
                // Creating a virtual environment
                sh '''
                    python -m venv venv
                '''
            }
        }
        stage('Install Dependencies') {
            steps {
                // Installing dependencies listed in requirements.txt within the virtual environment
                sh '''
                    . venv/bin/activate   # Activate the virtual environment
                    pip install -r requirements.txt  # Install dependencies within the virtual environment
                '''
            }
        }
        stage('Run Automation Tests') {
            steps {
                // Running the tests using pytest within the activated virtual environment
                sh '''
                    . venv/bin/activate   # Activate the virtual environment
                    pytest --maxfail=5 --disable-warnings  # Run the tests
                '''
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
