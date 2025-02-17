pipeline{
    agent any
    stages{

       stage("withdockercontainer") {


            steps{
                withDockerContainer(
                    images: "python3.12-alpine"
                    args: '--user root -u 0'
                ){
                    sh(
                        label: '=============='
                        script: '''
                                python -m pip install --no-cache -U -r requirements.txt
                                python test.py
                        '''
                    )
                }
            }
        }

        
    }

}