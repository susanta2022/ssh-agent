pipeline{

    agent any


    stages{

        stage("init"){

            steps{

                withDockerContainer(
                    image: 'python:3.11-alpine',
                    args: '--user root -u 0',

                )
                {
                    sh(
                        label: '=======python 3.11=========',
                        script: '''
                                python -m pip install --no-cache -U -r requirements.txt
                        '''
                    )
                }
            }


        }

        stage('deploy'){

            steps{
                withCredentials([usernamePassword(credentialsId:'dockercred' , usernameVariable: 'dockeruser' , passwordVariable: 'dockerpassword')])
                {
                    sh "docker login -u ${env.dockeruser} -p ${env.dockerpassword}",
                    sh "docker logout"
                }
            }
        }

    }
}