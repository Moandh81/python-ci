pipeline {
    agent any 
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
            }
        }
    }
    
}
