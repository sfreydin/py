pipeline{
    agent any
    stages{
        stage('build'){
            steps{
                sh """
                docker images
                echo "FROM alpine" > /opt/Dockerfile
                docker build -t locals/test-alpine -f /opt/Dockerfile .
                docker images
                """
            }
        }
    }
}
