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
    
    mensagem = event['pathParameters']['mensagem']
    
    body = {
         "Messagem alegre : ": str(mensagem)
    }
    
    sqs.send(str(body))
    sqsDest.send(str(body))
    
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def recebe_sqs_principal_imprimir(event, context):
    env = Variables()
    sqs = SqsHandler(env.get_sqs_url())
    
    msgs = sqs.getMessage(10)
    
    texto = str(msgs)

    if texto[2:18] == "ResponseMetadata":
        body = {
             "Resposta " : "Nao ha mensagens"
        }
    else:
        for msg in msgs['Messages']:
            body = {
                 "Resposta " : str(msg['Body'])
            }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    
    return response
    
def publica_topico(event, context):
    env =  Variables()
    sqsDest = SqsHandler(env.get_sqs_url_dest())
    
    msgs = sqsDest.getMessage(10)

    for msg in msgs['Messages']:
        publish_message_to_sns(str(msg['Body']))

# def publish_message_to_sns(topicArn: str ,message: str):
def publish_message_to_sns(message: str):
    sns = boto3.client('sns')

    env = Variables()
    topicu = env.get_arnvsf()
    print("Topic List: %s" % topicu)

    response = sns.publish(
        TopicArn=topicu,
        Message=str(message),    
    )
    print(response)