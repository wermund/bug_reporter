import os
from datetime import datetime

def generate_markdown_report(test_name, error, screenshot_path):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Use safe path by replacing :: with __ and creating full folder if needed
    filename = test_name.replace("::", "__").replace("/", "__") + ".md"
    report_dir = "reports"
    os.makedirs(report_dir, exist_ok=True)
    report_path = os.path.join(report_dir, filename)

    with open(report_path, "w") as f:
        f.write(f"# 🐞 Bug Report for `{test_name}`\n")
        f.write(f"- **Timestamp:** {timestamp}\n")
        f.write(f"- **Error:** `{error}`\n\n")
        if screenshot_path:
            f.write(f"![Screenshot]({screenshot_path})\n")

    return report_path
