#!/usr/bin/env
import fire
from awslib.wikiphrases import key_phrases


if __name__ == '__main__':
    fire.Fire(key_phrases)
    