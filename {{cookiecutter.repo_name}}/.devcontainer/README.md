# Instructions

## Installation

1. Install Docker on your machine
2. Install the  Visual Studio Code Remote - Containers extension

## Secrets Configuration

1. Create the `secrets` directory under the repository.
2. Create a file called `.ansible_password` under the `secrets` directory with your ansible password.
3. Create a file called `azure.env` with your azure environment variables:

```sh
export AZURE_CLIENT_ID=''
export AZURE_SECRET=''
export AZURE_TENANT=''
export AZURE_SUBSCRIPTION_ID=''
```