# intersight_example
[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/Miradot/intersight_example)

A prototype for anyone who wants to get started integrating with Intersight. Its based on the intersight_rest-Python library provided by Cisco.

## Use Case Description
This tool builds a brief overview of the hardware known by intersight and presents it to the user. This tool should make the life easier for anyone who wants to build a brief overview of the hardware known by intersight, but its main purpose is to demonstrate how to get started integrating with Intersight.

## Installation
these installation instructions assumes you have a python environment with python-pip installed.

```
pip install -r requirements.txt
```

## Configuration
In order to get authentication set up, you need to add an API key to your intersight environment. See [this link](https://community.cisco.com/t5/data-center-documents/intersight-api-overview/ta-p/3651994) for information on how to get this done. Once you've downloaded the secret_key and the api_key, save those to individual files and reference them using environment variables as described below:

```
export INTERSIGHT_PRIVATE_KEY_PATH="./intersight/secret_key"
export INTERSIGHT_PUBLIC_KEY_PATH="./intersight/api_key"
```

## Usage

```
python intersight_example.py
```

### DevNet resources
If you want to try this out in a demo-environment, have a look at the following resources

1. [Devnet Learning Labs](https://developer.cisco.com/learning/modules/intersight-rest-api)
2. [DevNet Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/a63216d2-e891-4856-9f27-309ca61ec862?diagramType=Topology) 

## Known issues

intersight_rest doesnt do proper exception handling, so in this tool an authentication error is going to be presented as a generic error.

## Getting help

If you have questions, concerns, bug reports, etc., please create an issue against this repository.

## Getting involved

This project is supposed to work as a tutorial on how to get started with Intersight. If you have any suggestions on what else to include, feel free to reach ut by creating an issue.

----

## Licensing info


`Copyright (c) 2020, Miradot AB`

This code is licensed under the MIT License. See [LICENSE](./LICENSE) for details.

----

## Credits and references

1. [intersight_rest](https://github.com/CiscoUcs/intersight-rest)

