pipeline {
    agent {
        docker {
            image 'python:3.9'  // Use Python Docker image
            args '-v /dev/shm:/dev/shm' // Optional: Shared memory for Chrome
        }
    }
    stages {
        stage('Clone Repository') {
            steps {
                // Cloning the repository that contains the automation code
                git 'https://github.com/akshaynikham/Automation-Pytest-Selenium-CICD.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Installing dependencies listed in requirements.txt
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Automation Tests') {
            steps {
                // Start Selenium Chrome standalone container
                script {
                    def seleniumContainer = docker.run('selenium/standalone-chrome', '-d -p 4444:4444')
                    // Wait for Selenium to be ready
                    sleep 10 // Adjust as needed based on your environment

                    // Run tests against the Selenium container
                    sh '''
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
