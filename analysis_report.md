# Comprehensive Analysis Report: Vendor Performance & Data Ingestion

## 1. Executive Summary
This report synthesizes the data ingestion process, exploratory data analysis (EDA), and vendor performance insights derived from the provided Jupyter Notebooks (`data_joining.ipynb`, `Explorartory Data Analysis.ipynb`, and `Vendor Performace Analysis.ipynb`). The primary goal of the analysis was to evaluate vendor performance based on key metrics such as total sales, profit margins, delivery lead times, and amount of capital locked in unsold inventory.

## 2. Data Ingestion & Database Construction
The data ingestion process, outlined in `data_joining.ipynb`, was conducted systematically to handle the large-scale datasets efficiently:
- **Data Loading:** Raw datasets (CSV format) encompassing `begin_inventory`, `end_inventory`, `purchase_prices`, `purchases`, `sales`, and `vendor_invoice` were incrementally processed in chunks (chunksize of 50,000) using Pandas.
- **Database Creation:** A localized SQLite database (`inventory.db`) was constructed. Incremental chunk loading allowed for the efficient insertion of millions of records into the database without overwhelming system memory.
- **Data Integration:** Once the database was populated, `sqlite3` and Pandas were used seamlessly to run SQL queries retrieving data tables directly for Exploratory Data Analysis and Feature Engineering.

## 3. Exploratory Data Analysis & Feature Engineering
Data retrieved from SQLite underwent aggregation and transformation to calculate key vendor performance indicators (KPIs) in `Vendor Performace Analysis.ipynb`:
- **Sales & Purchases Aggregation:** Total Sales Dollars, Sales Quantity, Purchase Dollars, and Purchase Quantity were grouped per vendor.
- **Profit Margin Calculation:** Computed as: 
  `((Total Sales - Total Purchases) / Total Sales) * 100`.
- **Lead Time (Receiving Time):** Calculated as the difference between `PODate` and `ReceivingDate` to define the average delivery processing time per vendor.
- **Inventory & Locked Capital:** Evaluated the total amount of unsold merchandise (`onHand` * `Price`) tied to each vendor.

## 4. Vendor Performance Insights
Based on the transformed metrics, the following insights were uncovered:

### 4.1. Top vendors by Sales and Volume
- Analysis shows a high dependency on a small number of top vendors for overall procurement and sales revenue.
- Top-earning vendors like **DIAGEO NORTH AMERICA INC**, **JIM BEAM BRANDS COMPANY**, and **PERNOD RICARD USA** heavily govern the total market share, making them critical for overall company revenue.

### 4.2. Delivery Lead Times
- Average receiving times vary significantly across vendors. Consistent monitoring of lead times is critical to ensuring smooth supply chain operations and minimizing out-of-stock scenarios.

### 4.3. Locked Capital in Unsold Inventory
- Vendors contributing heavily to unsold inventory value were identified (e.g., **DIAGEO NORTH AMERICA INC** with highly locked capital, corresponding to roughly $480.93K). 
- Managing the procurement volume from vendors with extremely high locked capital will be a necessary strategic move to free up resources.

## 5. Statistical Inference: Profit Margins
Hypothesis testing and confidence intervals were calculated to understand the relationship between vendor sales volume and profitability.

### 5.1. Confidence Intervals
- **Top Vendors 95% CI:** Mean 31.17% (Margin of 30.74% to 31.61%)
- **Low Vendors 95% CI:** Mean 41.55% (Margin of 40.48% to 42.62%)
- *Insight:* Low-performing vendors based on sales tend to maintain significantly higher profit margins. This may be due to premium pricing, niche products, or lower operational overheads.

### 5.2. Two-Sample T-Test
- **Null Hypothesis (H₀):** No significant difference in mean profit margins between top-performing and low-performing vendors.
- **Alternative Hypothesis (H₁):** Means are significantly different.
- **Results:** T-Statistic of -17.6440 and P-Value of 0.0000.
- **Conclusion:** We successfully reject the Null Hypothesis. There is a definitive, statistically significant difference in profit margin structures between high-sales and low-sales vendors. High-volume vendors may require price adjustments or cost-optimization strategies, whereas low-volume (high-margin) vendors might benefit from more aggressive marketing to scale operations.

## 6. Conclusion
The comprehensive analysis of the existing datasets reveals a well-oiled ingestion pipeline and provides actionable intelligence on vendor health. Stakeholders can use these statistical inferences to adjust purchasing strategies—balancing the reliability and high sales of top vendors against the superior profit margins of lower-volume vendors.
