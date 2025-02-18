pipeline{

    agent any

    stages{

        stage("init"){

            steps{

                withDockerContainer(
                    image: 'python:3.11-alpine',
                    args: '--user root -U 0',

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

    }
}