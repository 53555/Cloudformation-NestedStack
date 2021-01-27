#!/bin/bash
CF_HOME=$1
BUCKET_NAME=$2
REGION_NAME=$3
Network_Template=$(aws s3 ls s3://$BUCKET_NAME | awk -F" " '{print $4}'| grep NetworkStackStudent.yaml)
IAM_Template=$(aws s3 ls s3://$BUCKET_NAME | awk -F" " '{print $4}'| grep IAMRole.yaml)

if [[ $IAM_Template != "IAMRole.yaml" ]]
then
        aws s3 cp $CF_HOME/IAMRole.yaml s3://$BUCKET_NAME/ --region $REGION_NAME 
else
        echo "$IAM_Template already exist"
fi

if [[ $Network_Template != "NetworkStackStudent.yaml" ]]
then
        aws s3 cp $CF_HOME/NetworkStackStudent.yaml s3://$BUCKET_NAME/ --region $REGION_NAME 
else
        echo "$Network_Template already exist"
fi