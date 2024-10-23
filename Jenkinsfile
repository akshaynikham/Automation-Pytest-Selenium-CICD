pipeline {
    agent {
        docker {
            image 'python:3.9'  // Using Python Docker image
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
                // Creating virtual environment
                sh '''
                python -m venv venv
                . venv/bin/activate
                '''
                }
            }
        stage('Install Dependencies') {
            steps {
                // Installing dependencies listed in requirements.txt
                sh ''' 
                . venv/bin/activate
                pip install -r requirements.txt 
                '''
            }
        }
        stage('Run Automation Tests') {
            steps {
                // Start Selenium Chrome standalone container
                script {
                   sh 'docker run -d -p 4444:4444 --name selenium-chrome selenium/standalone-chrome'
                    // Wait for Selenium to be ready
                    sleep 10 // Adjust as needed based on your environment

                    // Run tests against the Selenium container
                    sh '''
                    . venv/bin/activate
                    pytest --maxfail=5 --disable-warnings \
                    --driver "http://localhost:4444/wd/hub" \
                    --headless
                    '''

                    // Stop the Selenium container after tests
                    seleniumContainer.stop()
                }
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
