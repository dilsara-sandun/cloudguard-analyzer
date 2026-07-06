\# CloudGuard 🛡️ – Local AWS IAM Privilege-Escalation \& Attack-Path Analyzer



CloudGuard is a fully local, high-performance static analysis security tool designed to identify and map AWS IAM privilege escalation attack paths. Inspired by Rhino Security Labs' research ("21 Ways to Escalate IAM Privileges"), this tool identifies dangerous misconfigurations before they hit production environments.



\---



\## 🎯 Architectural Concept \& Why This Project?

Traditional cloud security scanners require an active cloud connection, live billing setups, or credit card mapping. This poses financial and privacy risks for local testing. 



\*\*CloudGuard solves this by operating 100% locally with zero cloud costs and zero VM dependencies.\*\* 



It creates an autonomous mock AWS identity mesh purely inside temporary runtime buffers. It dynamically pulls permission definitions via native API structures and evaluates them using a programmatic rules engine. This design allows it to run smoothly on standard development laptops (like an 8GB RAM Windows environment) while demonstrating production-grade core logic engineering.



\---



\## 🛠️ Core Engine Pipeline \& Component Design

The project is built using a highly decoupled, modular architecture:



1\. \*\*Mock Execution Engine (`src/mock\_environment.py`)\*\*: Uses the `moto` library to simulate live, multi-tenant AWS identity meshes in memory, staging complex misconfigurations securely.

2\. \*\*Context-Aware Evaluator (`src/iam\_fetcher.py`)\*\*: Programmatically interrogates the mock environments using `boto3` API structures to extract active security policy schemas.

3\. \*\*Deterministic Rules Engine (`src/escalation\_rules.py`)\*\*: Executes deterministic rule assertions against extracted permissions to discover critical escalation vectors.

4\. \*\*Graph Topology Mapper (`src/graph\_builder.py`)\*\*: Transforms abstract permission matrices into multi-layered visual edge topologies using `networkx` and `matplotlib`.

5\. \*\*Data Compilation Engine (`src/report\_generator.py`)\*\*: Merges algorithmic finding structures with HTML templates via `jinja2` to compile executive remediation guides.



\---



\## 📊 Security Artifacts \& Automated Outputs



When executed, the system dynamically analyzes permissions and populates the `reports/` directory with two critical artifacts:



\### 1. `attack\_graph.png` (Structural Attack Vector Map)

Visually constructs the traversal boundary from an unprivileged identity to full infrastructure compromise:

\* 🔴 \*\*CRITICAL\*\*: Immediate identity promotion bypasses (e.g., `iam:AttachUserPolicy` abuse).

\* 🟠 \*\*HIGH\*\*: Secondary delegation or code execution hijacking (e.g., `iam:PassRole` + `lambda:CreateFunction`).



\### 2. `report.html` (Automated Executive Blueprint)

A comprehensive, client-ready HTML security report detailing:

\* \*\*The Vulnerable Entity\*\*: Targeted IAM Username.

\* \*\*Risk Threshold\*\*: Dynamic classification based on potential impact.

\* \*\*Technical Explanation\*\*: Step-by-step description of how an attacker can leverage the flaw.

\* \*\*Remediation Recommendation\*\*: Specific infrastructure-as-code adjustments required to mitigate the risk.



\---



\## ⚙️ Project Structure \& Directory Blueprint

```text

cloudguard-analyzer/

│

├── .github/workflows/

│   └── ci.yml                  # Autonomous GitHub Actions CI/CD Pipeline

├── src/

│   ├── templates/

│   │   └── report\_template.html # Jinja2 HTML Reporting Template

│   ├── mock\_environment.py     # Moto-based AWS simulation engine

│   ├── iam\_fetcher.py          # Boto3 logic for contextual data retrieval

│   ├── escalation\_rules.py     # Deterministic rules engine (Core Logic)

│   ├── graph\_builder.py        # NetworkX attack topology generator

│   └── report\_generator.py     # Audit reporting compilation pipeline

├── tests/

│   └── test\_escalation.py      # Quality assurance test suite

├── reports/                    # Auto-generated security artifacts

├── requirements.txt            # Project dependency manifestations

└── main.py                     # Main execution runtime driver

```



\---



\## 📥 Setup, Local Installation \& Execution



\### 1. Pre-requisites

\* Python 3.10 or higher installed.

\* Standard terminal tool (Windows Command Prompt or PowerShell).



\### 2. Isolate and Install Dependencies

```bash

\# Isolate environment context

python -m venv cloudguard-env

cloudguard-env\\Scripts\\activate



\# Install required external binary distributions

pip install boto3 moto networkx matplotlib jinja2 pytest

```



\### 3. Run the Security Scanner

```bash

python main.py

```



\### 4. Execute the Test Suite

Demonstrating enterprise-level reliability via isolated quality control testing:

```bash

python -m pytest tests/

```



\---



\## 🛡️ Evaluated Security Vectors (Roadmap Framework)

\* \*\*Vector 01 (CRITICAL)\*\*: Direct Identity Promotion via `iam:AttachUserPolicy` Abuse.

\* \*\*Vector 02 (HIGH)\*\*: Functional Compute Hijacking via `iam:PassRole` + `lambda:CreateFunction` Pipeline.

\* \*\*Vector 03 (HIGH)\*\*: Structural Definition Re-Mapping via `iam:CreatePolicyVersion` Privilege Escalation.



