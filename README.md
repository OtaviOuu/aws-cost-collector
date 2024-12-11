# AWS Cost Collector

This is a Serverless Framework project that collects and reports the total AWS cost on a regular schedule.

## Features

- Fetches the total AWS cost for the current month using the AWS Cost Explorer API
- Sends a message to a Telegram bot with the current month's total cost
- Runs on a schedule, either every minute or at 11:00 PM UTC daily

## Installation

1. Install the Serverless Framework: `npm install -g serverless`
2. Clone the repository: `git clone https://github.com/your-username/aws-cost-collector.git`
3. Navigate to the project directory: `cd aws-cost-collector`
4. Install dependencies: `serverless plugin install`
5. Configure your AWS credentials and Telegram bot settings in the `serverless.yml` file.
6. Deploy the service: `serverless deploy`

## Usage

The service will automatically run on the schedule you configured in the `serverless.yml` file. You can also invoke the function manually:

```
serverless invoke -f get_cost
```

This will trigger the function and send the current month's AWS cost to the Telegram bot.

## Configuration

The following configuration options are available in the `serverless.yml` file:

- `org`: The Serverless Framework organization name.
- `app`: The Serverless Framework app name.
- `service`: The name of the service.
- `provider.region`: The AWS region to deploy the service to.
- `provider.stage`: The deployment stage.
- `provider.iam.role.statements`: IAM permissions for the AWS Cost Explorer API.
- `functions.get_cost.events`: The schedule configuration for the function.
