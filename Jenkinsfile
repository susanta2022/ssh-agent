pipeline{
    agent any
    stages{

       stage("init") {
            agent {
                docker {
                    image 'maven:3.9.3-eclipse-temurin-17'
                    args '-u 0 -v /root/.m2:/root/.m2 -w /root/.m2'
                    //       reuseNode true
                }
            }
            steps {
                sh 'mvn dependency:get -Dartifact=org.springframework:spring-instrument:3.2.4.RELEASE'
                sh (
                    label: 'Clean and rebuild application distribution files',
                    script: '''
                                                                                    mkdir -p /home/ubuntu/susanta
                                                                       '''
                )
            }
        }
    }

}