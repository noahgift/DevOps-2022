import wikipedia
import boto3

def key_phrases(name):
    """comprehend and wikipedia"""
    text = wikipedia.summary(name)
    client = boto3.client('comprehend')
    response = client.detect_key_phrases(
        Text=text,
        LanguageCode='en'
    )
    return response['KeyPhrases']

    