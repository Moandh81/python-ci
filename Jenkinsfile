pipeline {
    agent any 
    
    

    
    stages {
        stage('Build') { 
            steps {
                echo 'this is the build step'
                sh 'ls -lh'
            }
            
        }
            
            stage ('Sonarqube') {
                
                steps {
                 
                    sh """
                    sonar-scanner \
  -Dsonar.projectKey=jenkins-sonarqube \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://13.37.255.229:9000 \
  -Dsonar.login=7acee38326bfb519b60a1a320c45520d6c3f39ed
                    
                    
                    """
                    
                    
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
