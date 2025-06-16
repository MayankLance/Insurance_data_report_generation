# Insurance Report Generator

This project generates synthetic insurance policy data and creates a PDF report with basic visualizations using Python.

## Project Structure

project-root/
├── input/
│   └── insurance_data.xlsx        # Source data (Excel)
├── output/
│   └── insurance_report.pdf       # PDF report (auto-generated)
├── scripts/
│   ├── generate_visualisation_doc.py  # Main Python script
│   └── run_report.bat             # Windows batch file
└── README.md                      # Instructions & usage


---

##  Requirements

Make sure Python is installed. Then install the following packages:

```bash
pip install pandas matplotlib seaborn faker openpyxl
```


How to Use
Automation
You can directly run the file run_report.bat under scripts to generate the file


**Report Visuals Included**

Policy Type Distribution

Product Distribution

Region-wise Policy Count

Premium Distribution (Histogram)

Channel vs Product Heatmap

 **Notes**
The data generated is fake and for demo purposes only.

All visualizations are saved directly into a multi-page PDF.
