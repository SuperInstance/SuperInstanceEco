G8vEZxzHqrrns6j3VJNKF1T1GbpFlD4=",
    "Version": "$LATEST",
    "TracingConfig": {
        "Mode": "PassThrough"
    },
    "RevisionId": "1458ab90-6867-4a73-a066-d34a7ae21c4b",
    "State": "Pending",
    "StateReason": "The function is being created.",
    "StateReasonCode": "Creating",
    "PackageType": "Zip",
    "Architectures": [
        "x86_64"
    ],
    "EphemeralStorage": {
        "Size": 512
    },
    "SnapStart": {
        "ApplyOn": "None",
        "OptimizationStatus": "Off"
    },
    "RuntimeVersionConfig": {
        "RuntimeVersionArn": "arn:aws:lambda:us-east-1::runtime:26afe95b80f712a3037463ff3166f54bef5aa010c870d7110cc2ce1e1233a3d5"
    },
    "LoggingConfig": {
        "LogFormat": "Text",
        "LogGroup": "/aws/lambda/activelog-logger"
    }
}


(venv) C:\Users\casey\activelog-deploy\lambda>
(venv) C:\Users\casey\activelog-deploy\lambda>aws lambda invoke --function-name activelog-logger --payload "{}" response.json --region us-east-1
{
    "StatusCode": 200,
    "FunctionError": "Unhandled",
    "ExecutedVersion": "$LATEST"
}


(venv) C:\Users\casey\activelog-deploy\lambda>aws lambda update-function-code --function-name activelog-logger --zip-file fileb://../dm_logger.zip --region us-east-1
{
    "FunctionName": "activelog-logger",
    "FunctionArn": "arn:aws:lambda:us-east-1:451523008183:function:activelog-logger",
    "Runtime": "python3.11",
    "Role": "arn:aws:iam::451523008183:role/ActivelogLambdaExecutionRole",
    "Handler": "dm_logger.lambda_handler",
    "CodeSize": 484,
    "Description": "",
    "Timeout": 3,
    "MemorySize": 128,
    "LastModified": "2025-08-16T17:30:54.000+0000",
    "CodeSha256": "qEhyKQRGBxMu9kwKxqCInbo0mSgf4oMsC8kH/KzDSW8=",
    "Version": "$LATEST",
    "TracingConfig": {
        "Mode": "PassThrough"
    },
    "RevisionId": "d8c50028-9872-4e87-bf8e-9e9675dac1fe",
    "State": "Active",
    "LastUpdateStatus": "InProgress",
    "LastUpdateStatusReason": "The function is being created.",
    "LastUpdateStatusReasonCode": "Creating",
    "PackageType": "Zip",
    "Architectures": [
        "x86_64"
    ],
    "EphemeralStorage": {
        "Size": 512
    },
    "SnapStart": {
        "ApplyOn": "None",
        "OptimizationStatus": "Off"
    },
    "RuntimeVersionConfig": {
        "RuntimeVersionArn": "arn:aws:lambda:us-east-1::runtime:26afe95b80f712a3037463ff3166f54bef5aa010c870d7110cc2ce1e1233a3d5"
    },
    "LoggingConfig": {
        "LogFormat": "Text",
        "LogGroup": "/aws/lambda/activelog-logger"
    }
}


(venv) C:\Users\casey\activelog-deploy\lambda>