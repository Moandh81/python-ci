pipeline {
    agent any 
    
    
    

    
    stages {
        stage('Build') { 
            steps {
                echo 'this is the build step'
                sh 'ls -lh'
            }
            
        }
        
        
        stage('Static Code Analysis'){
            
            steps {
    sh 'mvn clean verify sonar:sonar -Dsonar.projectName=jenkins-sonarqube    -Dsonar.projectKey=jenkins-sonarqube -Dsonar.projectVersion=$BUILD_NUMBER';
                
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
    
    
    post {
        
        success {
            echo "Cleaning up workspace"   
        }
        
    }
    
}
