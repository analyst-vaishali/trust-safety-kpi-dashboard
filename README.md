Trust & Safety KPI Dashboard | Tableau + Python
Dashboard
Overview
Executive-level KPI dashboard tracking 100 e-commerce sellers, detecting 349 ghost accounts, and segmenting risk categories. Built with Python data cleaning + Tableau Public.
Key Metrics:
349 ghost accounts detected
60% High Risk — Requires automated banning
43.09% Avg Approval Rate
53.53 hrs Avg Decision Time
Dashboard Components
KPI Cards (Top Row)
43.09% Avg. Approval Rate
349 Ghost Accounts
53.53 hrs Avg Decision Time
Risk Category Distribution
Treemap — Percent of Total
60% High Risk (Red) — 60 sellers — Action: Ban Account
21% Medium Risk (Yellow) — 21 sellers — Action: Manual Review
19% Low Risk (Green) — 19 sellers — Action: Approve
Tableau Skills: Percent of Total, Count(Seller ID)
Ghost Accounts by Seller Type
Bar chart sorted descending
BookNest: 82, HomeEssentials: 62, GadgetWorld: 62, ToyZone: 61, FashionHub: 43, Unknown: 39
Tableau Skills: Sort Descending, Color by Real Seller Type, Show Mark Labels
Approval Rate vs Fake Review Correlation
Scatter plot — Fake Review Ratio (X) vs Approval Rate % (Y)
Color: Risk Category (Red=High, Yellow=Medium, Green=Low)
Size: Ghost Accounts
Trend Lines: Linear trend per Risk Category
How I Built It
Step 1: Data Cleaning (Python)
Raw data had messy values like Seller_001, HomeEssentials, 11.6 percent, N/A, 5 ghost accounts - see notes
Cleaning functions in dashboard_cleaning_code.py:
clean_seller_id() — Remove emojis, HTML, special chars
clean_real_seller_type() — Standardize seller types
clean_number() — Convert text to number
clean_percentage() — Convert percent strings to float
clean_month() — Normalize dates
Step 2: Tableau Dashboard
Data: 100 rows cleaned
Charts:
Risk Category Treemap — 60%/21%/19%
Ghost Accounts Bar — 82/62/62/61/43/39, sorted descending
Approval vs Fake Review Scatter — With Size, Color, Trend Lines
KPI Cards — Measure Names/Values horizontal
Repository Structure
README.md
dashboard_cleaning_code.py
trust_safety_dashboard.png
trust_safety_dashboard_raw.xlsx
Skills
Python (pandas), Tableau Public (Percent of Total, Sort Descending, Measure Names/Values, Trend Lines, Scatter, Bar, Treemap, KPI Cards), Data Cleaning, KPI definition, Risk segmentation, Trust & Safety
Results
349 ghost accounts detected across 100 sellers
BookNest = 82 — Highest risk, needs immediate audit
60% High Risk — Need automated banning
Reduces review time from 4 hours to 30 mins
