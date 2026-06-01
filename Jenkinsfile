pipeline {

    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Install Playwright Browser') {
            steps {
                bat 'python -m playwright install'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }
    }
}
