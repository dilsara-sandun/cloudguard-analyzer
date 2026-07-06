from src.escalation_rules import detect_escalations

def test_detect_escalations_passrole_combo():
    """
    PassRole + CreateFunction
    """
    mock_user_data = {
        "test-hacker-user": ["iam:PassRole", "lambda:CreateFunction", "lambda:InvokeFunction"]
    }
    
    findings = detect_escalations(mock_user_data)
    
    assert "test-hacker-user" in findings
    assert len(findings["test-hacker-user"]) == 1
    assert findings["test-hacker-user"][0]["risk"] == "HIGH"
    assert "lambda:CreateFunction" in findings["test-hacker-user"][0]["name"]
