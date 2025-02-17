pipeline{
    agent any
    stages{

       stage("withdockercontainer") {

            // steps {
            //     echo "Using Docker image: python:3.11-buster"
                
            //         withDockerContainer(

            //             image: "python:3.11-alpine",
            //             args: '--user root -u 0 ',

            //         ) {
            //             sh(
            //                 label: '<<=======Copy source files into src-volume========>>',

            //                 script: '''    
            //                                 python -m pip install --no-cache -U -r requirements.txt
            //                                 python test.py

            //                                                       '''
            //             )
            //         }
              
            // }

            

            steps{
                withDockerContainer(
                    image: "python3.12-alpine",
                    args: '--user root -u 0',
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