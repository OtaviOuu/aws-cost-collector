import boto3
from datetime import datetime
from dateutil import relativedelta


from utils import send_message_to_telegram as send_message

session = boto3.Session()
ce_client = session.client("ce")


def get_cost(event, context):

    todayDate = datetime.now()
    initialDate = todayDate.strftime("%Y-%m-01")

    nextMonth = todayDate + relativedelta.relativedelta(months=1)
    finalDate = nextMonth.strftime("%Y-%m-01")

    response = ce_client.get_cost_and_usage(
        TimePeriod={
            "Start": initialDate,
            "End": finalDate,
        },
        Granularity="MONTHLY",
        Metrics=["AmortizedCost"],
    )
    cost = response["ResultsByTime"][0]["Total"]["AmortizedCost"]["Amount"]
    cost = round(float(cost), 2)

    message = f"Total AWS cost: ${cost}"

    send_message(message)
    return {"statusCode": 200, "body": message}


get_cost({}, {})
