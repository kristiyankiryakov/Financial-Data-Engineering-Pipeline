pipeline {
    agent any
    
    environment {
        // Python virtual environment
        VENV_NAME = 'stock_data_venv'
    }
    
    triggers {
        // Run once a day at midnight
        cron('0 0 * * *')
    }
    
    stages {
        stage('Setup Python Environment') {
            steps {
                script {
                    sh """
                        python3 -m venv ${VENV_NAME}
                        . ${VENV_NAME}/bin/activate
                        pip install -r ./requirements.txt
                    """
                }
            }
        }
        
        stage('Collect Stock Data') {
            steps {
                script {
                    sh """
                        . ${VENV_NAME}/bin/activate
                        python3 data_collector.py
                    """
                }
            }
        }
        
        stage('Upload to Azure') {
            steps {
                script {
                    sh """
                        . ${VENV_NAME}/bin/activate
                        python3 upload_raw_to_azure.py
                    """
                }
            }
        }
    }
    
    post {
        always {
            // Clean up virtual environment
            cleanWs()
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}