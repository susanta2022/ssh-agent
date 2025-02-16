pipeline{
    agent any
    stages{
        stage("A"){

            steps{
                
                sshagent(credentials: ['ansible']){
                            sh '''

                                ssh -o StrictHostKeyChecking=no node3@192.168.0.109 "ls -la" 

                            '''
                }
            }

        }
    }

}