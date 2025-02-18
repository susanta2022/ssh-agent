pipeline{

    agent any

    parameters{
        string(name: 'awsAccountId' , description: 'aws account id description')
        choice(name: 'registryHub' , choices: ['docker', 'ecr' , 'acr' , 'gcr'] , description: 'container images hub')
    }

    stages{

        stage("init"){



            steps{

                echo "==========${params.awsAccountId}============"

                withDockerContainer(
                    image: 'python:3.11-alpine',
                    args: '--user root -u 0',

                )
                {
                    sh(
                        label: '=======python 3.11=========',
                        script: '''
                                python -m pip install --no-cache -U -r requirements.txt
                                pytest -s  test_math_operations.py

                        '''
                    )
                }
            }


        }

        stage('deploy'){

            steps{
                withCredentials([usernamePassword(credentialsId: 'dockercred', usernameVariable:'dockeruser' , passwordVariable:'dockerpassword')]){
                    sh "docker login -u ${env.dockeruser} -p ${env.dockerpassword}"
                    sh "docker logout"
                }
            }
        }


        stage('sshconnection'){

            steps{

                sshagent(credentials: ['sshuser']){
                    sh(
                        labels: '=======ssh connection========',
                        script: '''
                            ssh -o StrictHostKeyChecking=no ubuntu@192.168.29.40 
                            "ls -la"

                        '''

                    )
                    
                }
            }
        }

    }
}