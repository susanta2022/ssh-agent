pipeline{
    agent any
    stages{

       stage("withdockercontainer") {

        steps{

            withDockerContainer(

                    image: "python:3.11-slim",
                    args: '--user root -u 0' ,

            ){


                sh(

                    label: 'test the application',

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