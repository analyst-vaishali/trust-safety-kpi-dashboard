
"""
Trust & Safety Dashboard - Data Cleaning Code
Project 3 - Cleaning RAW to CLEANED for Tableau
Author: Vaishali Desai
Tech: Python, Pandas, Regex - Same as Project 1 GhostStore!
"""

import pandas as pd
import re

# Load RAW messy data
df = pd.read_excel('trust_safety_dashboard_raw.xlsx', sheet_name='Seller_KPI_RAW')
print(f"Loaded {len(df)} raw sellers - messy data!")
print(df.head(3).to_string())

# === CLEANING FUNCTIONS (Same techniques as Project 1) ===

def clean_seller_id(text):
    """Remove emojis, extra text, keep Seller_XXX format"""
    # Remove emojis and extra text
    text = re.sub(r'[^a-zA-Z0-9_]', '', str(text))  # Keep only alphanumeric and _
    # Extract Seller_ pattern
    match = re.search(r'Seller_\d+', text)
    return match.group(0) if match else text

def clean_real_seller_type(text):
    """Map 20+ dirty variants to 5 real seller types (like GhostStore!)"""
    text = str(text).lower()
    # Remove HTML, emojis, extra spaces
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'[^a-z]', '', text)  # Keep only letters
    text = text.strip()
    
    # Mapping (same as Project 1!)
    if 'gadgetworld' in text or 'gadgetw0rld' in text or 'gadget' in text:
        return 'GadgetWorld'
    elif 'fashionhub' in text or 'fashion' in text:
        return 'FashionHub'
    elif 'toyzone' in text or 'toy' in text:
        return 'ToyZone'
    elif 'booknest' in text or 'book' in text:
        return 'BookNest'
    elif 'homeessentials' in text or 'home' in text:
        return 'HomeEssentials'
    else:
        return 'Unknown'

def clean_number(text, default=0):
    """Extract number from messy string like '5 ghost accounts - see notes' or '45%!!!'"""
    text = str(text)
    # Find first number (including decimal)
    match = re.search(r'\d+\.?\d*', text)
    if match:
        try:
            return float(match.group(0))
        except:
            return default
    return default

def clean_percentage(text):
    """Clean percentage: '45%', '45 percent', '0.45', 'N/A' -> 45.0"""
    text = str(text).lower()
    if 'n/a' in text or 'pending' in text or text.strip() == '':
        return 0.0
    
    num = clean_number(text, 0)
    # If number <1, it's probably decimal like 0.45 -> convert to 45
    if num < 1 and num > 0:
        num = num * 100
    return min(100, max(0, num))

def clean_region(text):
    """Clean region: 'INDIA', '<p>USA</p>', '  uk  ' -> India, USA, UK"""
    text = re.sub(r'<[^>]+>', '', str(text))
    text = text.strip().title()
    # Standardize
    mapping = {'India': 'India', 'Usa': 'USA', 'Uk': 'UK', 'Germany': 'Germany', 'Us': 'USA'}
    return mapping.get(text, text)

def clean_month(text):
    """Clean month: '2024-07-01', '07/08/2024', '2024/07' -> 2024-07"""
    text = str(text).strip()
    # Try to extract YYYY-MM
    match = re.search(r'(2024)[-/](\d{1,2})', text)
    if match:
        month = int(match.group(2))
        return f"2024-{month:02d}"
    # Try MM/YYYY
    match = re.search(r'(\d{1,2})[/-](2024)', text)
    if match:
        month = int(match.group(1))
        return f"2024-{month:02d}"
    return "2024-07"  # default

# === APPLY CLEANING (Like Project 1!) ===

print("\n=== CLEANING DATA ===")

df['Seller ID'] = df['Seller ID Raw'].apply(clean_seller_id)
df['Real Seller Type'] = df['Real Seller Type Raw'].apply(clean_real_seller_type)
df['Total Appeals'] = df['Total Appeals Raw'].apply(lambda x: int(clean_number(x, 0)))
df['Approval Rate %'] = df['Approval Rate Raw'].apply(clean_percentage)
df['Ghost Accounts'] = df['Ghost Accounts Raw'].apply(lambda x: int(clean_number(x, 0)))
df['Repeat Violations'] = df['Repeat Violations Raw'].apply(lambda x: int(clean_number(x, 0)))
df['Avg Decision Time (Hours)'] = df['Avg Decision Time Raw'].apply(lambda x: int(clean_number(x, 0)))
df['Fake Review Ratio'] = df['Fake Review Ratio Raw'].apply(lambda x: min(1, clean_number(x, 0) if clean_number(x,0) <=1 else clean_number(x,0)/100))
df['Risk Score'] = df['Risk Score Raw'].apply(lambda x: int(clean_number(x, 0)))
df['Account Age (Days)'] = df['Account Age Raw'].apply(lambda x: int(clean_number(x, 0)))
df['Region'] = df['Region Raw'].apply(clean_region)
df['Month'] = df['Month Raw'].apply(clean_month)

# Calculate Risk Category and Recommended Action (Business Logic)
def get_risk_category(score):
    if score >= 70:
        return "High Risk"
    elif score >= 40:
        return "Medium Risk"
    else:
        return "Low Risk"

def get_action(score):
    if score >= 70:
        return "Ban Account"
    elif score >= 50:
        return "Manual Review"
    elif score >= 30:
        return "Warning + Training"
    else:
        return "Approve"

df['Risk Category'] = df['Risk Score'].apply(get_risk_category)
df['Recommended Action'] = df['Risk Score'].apply(get_action)

# Keep only cleaned columns for Tableau
cleaned_df = df[['Seller ID', 'Real Seller Type', 'Total Appeals', 'Approval Rate %', 
                 'Ghost Accounts', 'Repeat Violations', 'Avg Decision Time (Hours)',
                 'Fake Review Ratio', 'Risk Score', 'Risk Category', 'Recommended Action',
                 'Account Age (Days)', 'Region', 'Month']]

print("\n=== CLEANED DATA (Ready for Tableau!) ===")
print(cleaned_df.head(5).to_string())

# Save cleaned version
cleaned_df.to_csv('seller_kpi_tableau_cleaned.csv', index=False)

with pd.ExcelWriter('trust_safety_dashboard_cleaned.xlsx', engine='openpyxl') as writer:
    cleaned_df.to_excel(writer, sheet_name='Seller_KPI_Cleaned', index=False)

print(f"\nSaved cleaned data: {len(cleaned_df)} sellers")
print("Files: seller_kpi_tableau_cleaned.csv, trust_safety_dashboard_cleaned.xlsx")
print("Ready for Tableau / Power BI!")
