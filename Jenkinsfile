pipeline{
    agent any
    stages{

       stage("withdockercontainer") {
            steps {
                echo "Using Docker image: python:3.11-buster"
                
                    withDockerContainer(

                        image: "python:3.11-buster",
              //           args: '--user root -u 0 -v ${WORKSPACE}:/usr/src/app',

                    ) {
                        sh(
                            label: '<<=======Copy source files into src-volume========>>',

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