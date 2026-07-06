from src.mock_environment import create_vulnerable_environment
from src.iam_fetcher import fetch_iam_data
from src.escalation_rules import detect_escalations
from src.graph_builder import build_attack_graph
from src.report_generator import generate_html_report
from moto import mock_aws

@mock_aws
def main():
    print("[*] Launching CloudGuard Local IAM Security Analyzer...")
    
    # 1. Initialize Mock AWS Environment
    print("[*] Initializing local vulnerable IAM simulation...")
    iam_client = create_vulnerable_environment()
    
    # 2. Fetch and Parse IAM Data
    print("[*] Scanning and parsing IAM security policies...")
    user_permissions = fetch_iam_data(iam_client)
    
    # 3. Run Rules Engine to detect patterns
    print("[*] Running Rhino Security Labs escalation detection rules...")
    findings = detect_escalations(user_permissions)
    
    # 4. Build and Save Attack Path Graph Image
    print("[*] Building attack-path visualization graph...")
    build_attack_graph(findings)
    
    # 5. Generate Professional HTML Report
    print("[*] Compiling final automated HTML audit report...")
    generate_html_report(findings)
    
    print("\n[+] Scan successfully completed!")
    print("[+] Attack Graph Saved: reports/attack_graph.png")
    print("[+] HTML Audit Report Saved: reports/report.html")

if __name__ == "__main__":
    main()
