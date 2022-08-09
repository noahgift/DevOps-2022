[![Python application test with Github Actions](https://github.com/noahgift/DevOps-2022/actions/workflows/main.yml/badge.svg)](https://github.com/noahgift/DevOps-2022/actions/workflows/main.yml)

[![code build](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiakljZmdVdldhd3VPaVpDMTdUMFp1S21RSktUMGttYzVsb1BvS1NiSUFybGVxbWcvNE05dUR3SWRsTHczVDRpVFdwNWhBRHRPOTVYNllyYTQ2KzhMZ0FRPSIsIml2UGFyYW1ldGVyU3BlYyI6IjRLSGxOVXNWUG9wVFhJOVYiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)

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

### Continuous Delivery with Code Build

```
version: 0.2

phases:
  #install:
  build:
    commands:
       - aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 561744971673.dkr.ecr.us-east-1.amazonaws.com
       - docker build -t fastapicd .
       - docker tag fastapicd:latest 561744971673.dkr.ecr.us-east-1.amazonaws.com/fastapicd:latest
       - docker push 561744971673.dkr.ecr.us-east-1.amazonaws.com/fastapicd:latest
```



