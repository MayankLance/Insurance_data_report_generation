import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Load the Excel data
df = pd.read_excel("D:\Insurance\input\insurance_data.xlsx")

# Create PDF file to save plots
pdf = PdfPages("D:\Insurance\output\insurance_report.pdf")

# 1. Policy Type Distribution
plt.figure(figsize=(6, 4))
sns.countplot(x='policy_type', data=df)
plt.title('Policy Type Distribution')
pdf.savefig()
plt.close()

# 2. Product Distribution
plt.figure(figsize=(8, 4))
sns.countplot(x='product', data=df, order=df['product'].value_counts().index)
plt.title('Product Distribution')
pdf.savefig()
plt.close()

# 3. Region-wise Policies
plt.figure(figsize=(6, 4))
sns.countplot(x='region', data=df, order=df['region'].value_counts().index)
plt.title('Region-wise Policy Count')
pdf.savefig()
plt.close()

# 4. Premium Distribution
plt.figure(figsize=(6, 4))
sns.histplot(df['premium'], bins=30, kde=True)
plt.title('Premium Distribution')
pdf.savefig()
plt.close()

# 5. Channel vs Product Heatmap
channel_product = pd.crosstab(df['channel'], df['product'])
plt.figure(figsize=(8, 5))
sns.heatmap(channel_product, annot=True, fmt='d', cmap='Blues')
plt.title('Channel vs Product')
pdf.savefig()
plt.close()

# Save PDF
pdf.close()
print("insurance_report.pdf created with basic visualizations.")
