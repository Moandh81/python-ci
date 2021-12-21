pipeline {
    agent any 
    
    
    environment {
REGISTRY_CREDENTIALS= credentials('docker registry')
REGISTRY_URL = 'https://hub.docker.com/'
}
    
    stages {
        stage('Build') { 
            steps {
                echo 'this is the build step'
                sh 'ls -lh'
            }
        }
        stage('Test') { 
            steps {
                echo 'this is the build step'
                sh 'ls -lh'
            }
        }
        stage('Deploy') { 
            steps {
               
               echo 'this is the Deploy step'
                sh 'ls -lh'
                sh 'docker --version'
                sh ' docker login --username $REGISTRY_CREDENTIALS_USR --password $REGISTRY_CREDENTIALS_PSW'
            }
        }
    }
    
    
    post {
        
        success {
            echo "Cleaning up workspace"   
        }
        
    }
    
}
