import os
from jinja2 import Template

def generate_html_report(all_findings):
    # Read HTML template from the external file securely
    template_path = os.path.join(os.path.dirname(__file__), 'templates', 'report_template.html')
    
    with open(template_path, 'r', encoding='utf-8') as template_file:
        html_template_content = template_file.read()
        
    template = Template(html_template_content)
    html_output = template.render(all_findings=all_findings)
    
    os.makedirs("reports", exist_ok=True)
    with open("reports/report.html", "w", encoding="utf-8") as f:
        f.write(html_output)
