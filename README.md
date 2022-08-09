# DevOps-2022
This is a repo for DevOps

## Process for Prototyping

1.  Try idea out in IPython
2.  Make a function
3.  Build a command-line tool.


## How to use Boto3 and AWS to Translate

[Boto3 Translate Docs](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate.html#Translate.Client.translate_text)

[API Languages](https://docs.aws.amazon.com/translate/latest/dg/API_ListLanguages.html)

```
response = client.translate_text(
    Text='string',
    TerminologyNames=[
        'string',
    ],
    SourceLanguageCode='string',
    TargetLanguageCode='string',
    Settings={
        'Formality': 'FORMAL'|'INFORMAL',
        'Profanity': 'MASK'
    }
)
```

Example of text:

```python
text = """Lambda is a compute service that lets you 
    run code without provisioning or managing servers."""
```

