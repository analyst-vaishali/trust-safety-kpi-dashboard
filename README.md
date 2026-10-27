# Trust & Safety KPI Dashboard | Tableau + Python

[Dashboard](dashboard/trust_safety_dashboard_ULTRA_CLEAN.png)

## Overview
Executive-level KPI dashboard tracking **100 e-commerce sellers**, detecting **349 ghost accounts**, and segmenting risk categories. Built with **Python data cleaning + Tableau Public**.

**Key Metrics:**
- **349 ghost accounts** detected — Total fake accounts across all sellers
- **60% High Risk** — Requires automated banning workflow
- **43.09% Avg Approval Rate** — Indicates strict fraud controls
- **53.53 hrs Avg Decision Time** — Opportunity to automate

## Dashboard Components

### KPI Cards (Top Row)
- **43.09%** Avg. Approval Rate — Overall seller approval rate
- **349** Ghost Accounts — Total fake accounts detected
- **53.53 hrs** Avg Decision Time — Average time to review seller

### Risk Category Distribution
- **Treemap visualization** with Percent of Total calculation
- **60% High Risk (Red)** — 60 sellers — Action: Ban Account
- **21% Medium Risk (Yellow)** — 21 sellers — Action: Manual Review
- **19% Low Risk (Green)** — 19 sellers — Action: Approve
- **Tableau Skills:** Percent of Total, Count(Seller ID)

### Ghost Accounts by Seller Type
- **Bar chart sorted descending** — Highest fraud sellers on left
- **BookNest: 82**, HomeEssentials: 62, GadgetWorld: 62, ToyZone: 61, FashionHub: 43, Unknown: 39
- **Tableau Skills:** Sort Descending, Color by Real Seller Type, Show Mark Labels
- **Insight:** Book category has most ghost accounts — possible review manipulation

### Approval Rate vs Fake Review Correlation
- **Scatter plot** — Fake Review Ratio (X) vs Approval Rate % (Y)
- **Color:** Risk Category (Red=High, Yellow=Medium, Green=Low)
- **Size:** Ghost Accounts — Bigger dot = more ghost accounts
- **Trend Lines:** Linear trend per Risk Category
- **Insight:** As Fake Review Ratio increases, Approval Rate decreases — High Risk sellers maintain high approval despite high fake reviews, indicating fraud signal

## How I Built It

### Step 1: Data Cleaning (Python)
Raw data had messy values like `Seller_001🔥`, `<b>HomeEssentials</b>`, `11.6 percent`, `N/A`, `5 ghost accounts - see notes`

**Cleaning functions in `code/dashboard_cleaning_code.py`:**
- `clean_seller_id()` — Remove emojis, HTML, special chars
- `clean_real_seller_type()` — Standardize seller types
- `clean_number()` — Convert "5 ghost accounts - see notes" → 5
- `clean_percentage()` — "11.6 percent" → 11.6
- `clean_month()` — Normalize dates
- `get_risk_category()` — Risk Score ≥70 = High, ≥40 = Medium, else Low
- `get_action()` — Risk-based recommended action

### Step 2: Tableau Dashboard
- **Data:** `seller_kpi_cleaned.csv` (100 rows)
- **Charts:**
  1. Risk Category Distribution — Treemap 60%/21%/19%
  2. Ghost Accounts by Seller Type — Bar chart 82/62/62/61/43/39, sorted descending
  3. Approval vs Fake Review Scatter — With Size=Ghost Accounts, Color=Risk, Trend Lines
  4. KPI Cards — Measure Names/Values horizontal layout

- **Dashboard Assembly:**
  - Tiled layout
  - Size: Automatic → Entire View
  - Containers: Vertical + Horizontal for clean layout

## Repository Structure
```
trust-safety-kpi-dashboard/
├── data/
│   ├── trust_safety_dashboard_raw.xlsx
│   └── seller_kpi_cleaned.csv
├── code/
│   └── dashboard_cleaning_code.py
├── dashboard/
│   └── trust_safety_dashboard_ULTRA_CLEAN.png
└── README.md
```

## Skills Demonstrated

**Technical:** Python (pandas), Tableau Public (Percent of Total, Sort Descending, Measure Names/Values, Containers, Trend Lines, Scatter, Bar, Treemap, KPI Cards), Data Cleaning

**Business Analysis:** KPI definition, Risk segmentation, Correlation analysis, Business impact (Reduce 4hrs to 30mins), Recommended Actions

**Trust & Safety Domain:** Ghost account detection, Fake review manipulation, Seller risk scoring, Fraud pattern identification

## Results
- **349 ghost accounts** detected across 100 sellers
- **BookNest identified as highest risk** (82 ghost accounts)
- **60% High Risk sellers** — Need automated banning
- **Dashboard reduces review time** from 4 hours to 30 mins

## Related Projects
1. **Operation GhostStore Fraud Detection** — Python, 500 messy sellers → 5 real sellers, 30 ghost accounts
2. **YouTube Monetization Appeal Risk Classifier** — NLP + Legal Reasoning, 60 appeals, 85% accuracy
3. **Trust & Safety KPI Dashboard (This Repo)** — Tableau + Python, 100 sellers, 349 ghosts
