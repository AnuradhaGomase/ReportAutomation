# Report Automation

This project is made to simplify reports generation process to reduce manual efforts using Python, YAML, Jinja2 and HTML.

## Project Screen Shots
Report_Generator.bat file output in cmd, you can choose additional tasks to include in your report
![image](https://github.com/user-attachments/assets/f7f509e2-c556-498f-b08f-ad2b158d59aa)

After tasks are choosen
![image](https://github.com/user-attachments/assets/4138229c-09cc-427d-a034-3764a28b3423)

Sample Report generated

![image](https://github.com/user-attachments/assets/a9f7a709-53b0-45df-8b56-873ccdf3bb58)


## Installation and Setup Instructions

Clone down this repository. 

Prerequisites:
You'll need to install two Python libraries:
pip install PyYAML Jinja2

PyYAML: To read and parse our .yml data hub file.
Jinja2: To use a powerful templating engine for our HTML report.

To Generate reports:

Create YYYY-MM-DD.yml file and run Report_Generator.bat

## Description

This project is made to reduce manual efforts while creating reports. This is made using Python, HTML, YAML and Jinja2. 
The template is made using HTML acting as a blueprint of report, it also uses Jinja2 syntax to get the daily info needed for report. 
The python file(generate_report.py) extracts information from YYYY-MM-DD.yml and recurring_tasks.yml and helps data render in HTML template using Jinja2.
When we run Report_Generator.bat, the report is created in format report_YYYY-MM-DD.
