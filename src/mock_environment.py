import boto3
import json
from moto import mock_aws

@mock_aws
def create_vulnerable_environment():

    iam = boto3.client("iam", region_name="us-east-1")

    # --- Scenario 1: PassRole + CreateFunction (High Risk) ---
    iam.create_user(UserName="dev-ci-user")
    policy_1 = {
        "Version": "2012-10-17",
        "Statement": [
            {"Effect": "Allow", "Action": ["iam:PassRole"], "Resource": "*"},
            {"Effect": "Allow", "Action": ["lambda:CreateFunction", "lambda:InvokeFunction"], "Resource": "*"}
        ]
    }
    iam.put_user_policy(
        UserName="dev-ci-user",
        PolicyName="LambdaDeployPolicy",
        PolicyDocument=json.dumps(policy_1)
    )

    # --- Scenario 2: AttachUserPolicy Self-Escalation (Critical Risk) ---
    iam.create_user(UserName="support-staff")
    policy_2 = {
        "Version": "2012-10-17",
        "Statement": [
            {"Effect": "Allow", "Action": ["iam:AttachUserPolicy"], "Resource": "*"}
        ]
    }
    iam.put_user_policy(
        UserName="support-staff",
        PolicyName="SupportEscalatePolicy",
        PolicyDocument=json.dumps(policy_2)
    )

    # --- Scenario 3: CreateNewPolicyVersion (High Risk) ---
    iam.create_user(UserName="junior-admin")
    policy_3 = {
        "Version": "2012-10-17",
        "Statement": [
            {"Effect": "Allow", "Action": ["iam:CreatePolicyVersion"], "Resource": "*"}
        ]
    }
    iam.put_user_policy(
        UserName="junior-admin",
        PolicyName="EditPolicyVersion",
        PolicyDocument=json.dumps(policy_3)
    )

    return iam
