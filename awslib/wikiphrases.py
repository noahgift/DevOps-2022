import wikipedia
import boto3
import wikipedia

def key_phrases(name):
    """comprehend and wikipedia"""
    text = wikipedia.summary("Golden_State_Warriors")
    client = boto3.client('comprehend')
    response = client.detect_key_phrases(
        Text=text,
        LanguageCode='en'
    )
    return response['KeyPhrases']

    