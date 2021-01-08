pipeline {
    agent any
    parameters {
        string(name: 'profile_name', defaultValue: 'admin1', description: 'Provide your profile name if it is configured')
        string(name: 'region_name', defaultValue: 'us-east-2', description: 'Provide your region name where you want to deploy your bucekt')
        string(name: 'bucket_name', defaultValue: 'student-cloudformation-template', description: 'Provide your bucket name you want to ceate to')
    }
    stages {
        stage('SCM CheckOut') {
            steps {
                git credentialsId: 'GitHub', url: 'https://github.com/53555/Cloudformation-NestedStack'
                sh 'echo "${WORKSPACE}"'
            }
        }
        stage('Deploy S3 Bucket "${bucket_name}" into AWS Account') {
            steps {
                sh 'python3 "${WORKSPACE}"/s3_upload.py $profile_name $region_name $bucket_name'
            }
        }
        stage('Upload nested stacks Templates into S3 Bucket ${bucket_name}') {
            environment {
                CF_HOME = "${WORKSPACE}"
                
            }
            steps {
                echo "${CF_HOME}"
                sh 'bash s3_object_upload.sh "${CF_HOME}" ${bucket_name} ${region_name}'
            }
        }
        stage('Deploy CloudFormation Stack into AWS') {
            steps {
                sh '''
                    aws cloudformation create-stack --stack-name AppStack-Layer --template-body file://"${WORKSPACE}"/Appstack_student_http.yaml --role-arn arn:aws:iam::191155221734:role/Appstack-Cloudformation-Role --capabilities CAPABILITY_NAMED_IAM --region ${region_name}

                    aws cloudformation wait stack-create-complete --stack-name AppStack-Layer --region ${region_name}

                    aws cloudformation describe-stack-events --stack-name AppStack-Layer --region ${region_name}
                   '''
            }
        }
    }
}
