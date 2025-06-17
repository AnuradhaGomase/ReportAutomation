import yaml
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import base64 # Import the base64 library for image encoding

# --- Configuration ---
today_str = datetime.now().strftime('%Y-%m-%d')
DATA_FILE = f"{today_str}.yml" 
RECURRING_TASKS_FILE = "recurring_tasks.yml"
LOGO_FILE = "app_logo.png" # Path to your logo file
TEMPLATE_FILE = "template.html"
OUTPUT_FILE = f"report_{today_str}.html"

# --- 1. Function to encode the logo ---
def encode_image(filepath):
    """Encodes an image file into Base64 for HTML embedding."""
    try:
        with open(filepath, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"Warning: Logo file not found at '{filepath}'. Logo will be missing.")
        return None

# --- 2. Load and Process All Data ---
all_work_items = []

# Load daily data (bugs and regular tasks)
try:
    with open(DATA_FILE, 'r') as f:
        daily_data = yaml.safe_load(f)
        all_work_items.extend(daily_data.get('work_items', []))
except FileNotFoundError:
    print(f"INFO: Daily data file '{DATA_FILE}' not found.")
    daily_data = {}

# Load and select recurring tasks (interactive part)
try:
    with open(RECURRING_TASKS_FILE, 'r') as f:
        recurring_data = yaml.safe_load(f)
        available_tasks = recurring_data.get('recurring_tasks', [])

    if available_tasks:
        print("\n--- Select Recurring Tasks to Include ---")
        for i, task in enumerate(available_tasks):
            print(f"  [{i+1}] {task['title']}")
        
        user_input = input("\nWhich tasks were performed today? (e.g., '1, 3' or leave blank): ")
        if user_input:
            selected_indices = [int(i.strip()) - 1 for i in user_input.split(',')]
            for index in selected_indices:
                if 0 <= index < len(available_tasks):
                    all_work_items.append(available_tasks[index])
except FileNotFoundError:
    pass # Silently ignore if no recurring tasks file

# --- 3. Separate Bugs from Tasks and Count Bugs ---
bugs_list = [item for item in all_work_items if item.get('type', '').lower() == 'bug']
tasks_list = [item for item in all_work_items if item.get('type', '').lower() != 'bug']
bug_count = len(bugs_list)

print(f"\nFound {bug_count} bug(s) and {len(tasks_list)} task(s).")

# --- 4. Prepare data for the template ---
logo_base64 = encode_image(LOGO_FILE)

template_data = {
    'report_date': daily_data.get('report_date', today_str),
    'builds': daily_data.get('build_details', []),
    'test_coverage': daily_data.get('test_cov', []),
    'ocv': daily_data.get('ocv', []),
    'bugs': bugs_list,
    'bug_count': bug_count,
    'tasks': tasks_list,
    'logo_base64': logo_base64
}

# --- 5. Render and Save the Final Report ---
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template(TEMPLATE_FILE)

print("Generating the HTML report with new layout...")
report_html = template.render(template_data)

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(report_html)

print(f"Success! Professional report saved as '{OUTPUT_FILE}'.")