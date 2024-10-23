pipeline {
    agent {
        docker {
            image 'python:3.9'
        }
    }
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/akshaynikham/Automation-Pytest-Selenium-CICD.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Automation Tests') {
            steps {
                script {
                    def seleniumContainer = docker.run('selenium/standalone-chrome', '-d -p 4444:4444')
                    sleep 10
                    sh '''
                    pytest --maxfail=5 --disable-warnings \
                    --driver "http://localhost:4444/wd/hub" \
                    --headless
                    '''
                    seleniumContainer.stop()
                }
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
