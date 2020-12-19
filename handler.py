import sys
sys.path.insert(0,'/opt')

import json
import boto3
import os

from sqsHandler import SqsHandler
from env import Variables

def inseresqs(event, context):
    env = Variables()
    sqs = SqsHandler(env.get_sqs_url())
    sqsDest = SqsHandler(env.get_sqs_url_dest())
    
    # mensagem = event['pathParameters']['mensagem']
    
    # body = {
    #     "message": str(mensagem)
    # }
    
    #sqs.send(str(mensagem))
    sqs.send(str("Vai tomate cru"))
    sqsDest.send(str("Vai tomate cru"))

def recebe_sqs_principal_imprimir(event, context):
    env = Variables()
    sqs = SqsHandler(env.get_sqs_url())
    
    mensagem = sqs.getMessage(1)
    
    print('Received message: %s' % mensagem)
    
def publica_topico(event, context):
    env =  Variables()
#    sqs = SqsHandler(env.get_sqs_url())
    sqsDest = SqsHandler(env.get_sqs_url_dest())
    
    msgs = sqsDest.getMessage(10)

    for msg in msgs['Messages']:
    # for msg in msgs:
        # message_content = json.loads(msg)
        #response = sns.publish(
        #opicArn='arn:aws:sns:us-east-1:559972492049:sns-topic-dev',    
        #Message=str(msg['Body']),
        # print(str(msg['Body']))
        publish_message_to_sns(str(msg['Body']))
        # publish_message_to_sns(str(message_content['TopicArn']),str(message_content['Message']))
    #print(response)

# def publish_message_to_sns(topicArn: str ,message: str):
def publish_message_to_sns(message: str):
    # print(str(message))
    # topic_arn = 'arn:aws:sns:us-east-1:559972492049:sns-topic-dev'

    # sns_client = boto3.client(
    #     "sns",
    #     region_name="us-east-1",
    # )

    # message_id = sns_client.publish(
    #     TopicArn=topic_arn,
    #     Message=message,
    # )
    
    # print(str(message_id))
    
    # return message_id
    # Create an SNS client
    sns = boto3.client('sns')
    #session = boto3.session.Session()
    #print("session : " + str(session))
    #client = session.client('sns', 'us-east-1')
    #print("client : " + str(client))
    #topicArn = client.list_topics()['Topics'][0]['TopicArn'][0]
    #topicArn = client.list_topics()['Topics']
    #print("Topico : " + str(topicArn))
    
    env = Variables()
    topicu = env.get_arnvsf()
    #resp = sns.list_topics()
    #topics = [topic['TopicArn'] for topic in response['Topics']]
    print("Topic List: %s" % topicu)

    # Publish a simple message to the specified SNS topic
    response = sns.publish(
        # TopicArn=str(topicArn),
        # TopicArn='arn:aws:sns:us-east-1:559972492049:Meutopicu',
        TopicArn=topicu,
        Message=str(message),    
    )

    # Print out the response
    print(response)