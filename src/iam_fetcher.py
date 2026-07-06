import json

def fetch_iam_data(iam_client):
    extracted_data = {}
    users_response = iam_client.list_users()

    for user in users_response['Users']:
        username = user['UserName']
        extracted_data[username] = []

        inline_policies = iam_client.list_user_policies(UserName=username)
        for policy_name in inline_policies['PolicyNames']:
            policy_detail = iam_client.get_user_policy(UserName=username, PolicyName=policy_name)
            doc = policy_detail['PolicyDocument']
            if isinstance(doc, str):
                doc = json.loads(doc)
            for statement in doc.get('Statement', []):
                actions = statement.get('Action', [])
                if isinstance(actions, str):
                    actions = [actions]
                if statement.get('Effect') == 'Allow':
                    extracted_data[username].extend(actions)
    return extracted_data
