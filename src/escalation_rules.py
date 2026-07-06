KNOWN_ESCALATION_COMBOS = [
    {
        "name": "iam:PassRole + lambda:CreateFunction",
        "required_actions": {"iam:PassRole", "lambda:CreateFunction"},
        "risk": "HIGH",
        "explanation": "User can pass a privileged IAM role to a new Lambda function and execute admin-level code via function invocation.",
        "remediation": "Restrict iam:PassRole to specific trusted resource ARNs only. Enforce least privilege on Lambda configurations."
    },
    {
        "name": "iam:AttachUserPolicy Self-Escalation",
        "required_actions": {"iam:AttachUserPolicy"},
        "risk": "CRITICAL",
        "explanation": "User can attach the AdministratorAccess policy to their own identity, achieving full administrative privileges.",
        "remediation": "Restrict iam:AttachUserPolicy permissions. Use IAM Permissions Boundaries to restrict maximum obtainable privileges."
    },
    {
        "name": "iam:CreatePolicyVersion Privilege Escalation",
        "required_actions": {"iam:CreatePolicyVersion"},
        "risk": "HIGH",
        "explanation": "User can create a new version of an existing policy that defines open permissions like '*' (All Actions), then set it as default.",
        "remediation": "Do not grant iam:CreatePolicyVersion unless strictly necessary, and audit historical policy versions regularly."
    }
]

def detect_escalations(user_permissions_dict):
    all_findings = {}

    for username, actions in user_permissions_dict.items():
        user_action_set = set(actions)
        all_findings[username] = []

        for combo in KNOWN_ESCALATION_COMBOS:
            if combo["required_actions"].issubset(user_action_set):
                all_findings[username].append({
                    "name": combo["name"],
                    "risk": combo["risk"],
                    "explanation": combo["explanation"],
                    "remediation": combo["remediation"]
                })
                
    return all_findings
