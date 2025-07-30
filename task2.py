import pandas as pd
from fpdf import FPDF

# Load data from a CSV file
data = pd.read_csv("sample_data.csv")

# Perform basic analysis (summary statistics)
summary = data.describe()

# Create PDF report
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Automated Data Report", ln=True, align="C")
        self.ln(10)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 10, body)
        self.ln()

# Generate PDF
pdf = PDF()
pdf.add_page()
pdf.chapter_title("Summary Statistics")
pdf.chapter_body(summary.to_string())

# Save the PDF
pdf.output("sample_report.pdf")

print("PDF report generated as 'sample_report.pdf'")
