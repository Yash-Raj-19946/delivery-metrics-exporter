
pipeline {
    agent any

    stages {

        stage('Source Checkout') {
            steps {
                echo 'Checking out source code from GitHub'
                checkout scm
                bat 'dir'
            }
        }

        stage('Dependency Installation') {
            steps {
                echo 'Checking Python installation'
                bat 'py -3 --version'

                echo 'Creating virtual environment'
                bat 'py -3 -m venv .venv'

                echo 'Installing dependencies'
                bat '.venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat '.venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Automated Testing') {
            steps {
                echo 'Running automated tests'
                bat '.venv\\Scripts\\python.exe -m unittest test_metrics -v'
            }
        }

        stage('Deployment Packaging') {
            steps {
                echo 'Creating deployment package'

                bat '''
                if exist deployment rmdir /S /Q deployment
                mkdir deployment

                copy /Y metrics_exporter.py deployment\\
                copy /Y requirements.txt deployment\\
                copy /Y README.md deployment\\

                xcopy config deployment\\config\\ /E /I /Y
                '''

                archiveArtifacts artifacts: 'deployment/**',
                                 fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'PIPELINE COMPLETED SUCCESSFULLY'
        }

        failure {
            echo 'PIPELINE FAILED - CHECK CONSOLE OUTPUT'
        }

        always {
            echo 'Jenkins execution finished'
        }
    }
}
