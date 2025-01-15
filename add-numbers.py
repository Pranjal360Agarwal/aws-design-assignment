def lambda_handler(event, context):
    num1 = event.get('num1', 0)
    num2 = event.get('num2', 0)
    result = num1 + num2
    return {
        'statusCode': 200,
        'body': f"The sum of {num1} and {num2} is {result}"
    }