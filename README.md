# 🧵 Serverless `Strands Weather Agent`
This is a simple serverless agent that uses weather and location APIs to get the weather information for a given location.
It is built with `Strands Agents SDK` using `http_request` tool and `AWS Bedrock` with `Amazon Nova Micro` model integration.

## ⚙️ Prerequisites
- [Python](https://www.python.org/downloads/) (v3.12 or later) (for the Python Lambda function)
- [Node.js](https://nodejs.org/en/download/) (v20 or later)
- [Serverless Framework](https://www.serverless.com/framework/docs/getting-started/) (v3 or later)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) (v2 or later)
- [AWS Account](https://aws.amazon.com/free/) (with IAM permissions to deploy Lambda functions)
- [AWS credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html) configured on your machine

## ⚙️ Setup
Run the following commands to set up the project:
```bash
npm install
```

## 🧪 Test the function locally
Use the Serverless Framework to invoke the function locally. You can use the `--data` flag to pass a JSON object with the `prompt` field containing your query.
```bash
sls invoke local -f weather --data '{"prompt": "What is the weather in Seattle?"}'
```

You can also use the region field (with option "US" or "IT") to specify the region for the weather query:
```bash
sls invoke local -f weather --data '{"prompt": "What is the weather in Pavia?", "region": "IT"}'
```

## 🚀 Deploy on AWS
Make sure you have configured your AWS credentials and have the necessary permissions to deploy Lambda functions. 

You can read more about configuring AWS credentials in the [AWS CLI documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)
or use the `aws configure` command to set them up interactively.

You can also use serverless framework to set up your AWS credentials by running:
```bash
sls config credentials --provider aws --key YOUR_AWS_ACCESS_KEY_ID --secret YOUR_AWS_SECRET_ACCESS_KEY
```

Then, run the following command to deploy the function to AWS:
```bash
sls deploy
```

