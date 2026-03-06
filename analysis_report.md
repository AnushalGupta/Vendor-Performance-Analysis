# Comprehensive Analysis Report: Vendor Performance & Data Ingestion

## 1. Executive Summary
This report synthesizes the data ingestion process, exploratory data analysis (EDA), and vendor performance insights derived from the provided analytics workflows. The primary goal of the analysis was to evaluate vendor performance based on key metrics such as total sales, profit margins, delivery lead times, and capital locked in unsold inventory.

## 2. Data Ingestion & Database Construction
To handle the large-scale datasets efficiently, a structured ingestion and optimization pipeline was implemented:
- **Data Tables:** Core data resides across multiple tables, including the `purchases` table (actual purchase transactions), `purchase_prices` (product-wise tracking), `vendor_invoice` (aggregated quantities and freight costs), and `sales` (transaction details and revenue earned).
- **Summary Optimization:** Because the required analysis spans multiple large tables, a consolidated summary table (`vendor_sales_summary`) was created containing purchase transactions, sales data, freight costs, and exact pricing. 
- **Performance Benefits:** Pre-aggregating heavy joins across massive sales and purchase tables avoids repeated expensive computations. This optimization ensures that dashboards and BI reporting tools can fetch data quickly and efficiently.

## 3. Exploratory Data Analysis (EDA)
In this phase of EDA, we analyzed the resultant summary table to gain insights into the distribution of each column, ultimately identifying anomalies and ensuring data quality before further hypothesis testing.

![Distribution Histograms](images/Screenshot%202026-03-06%20224048.png)
![Boxplots](images/Screenshot%202026-03-06%20224107.png)
![KDE Distributions](images/Screenshot%202026-03-06%20224133.png)

### 3.1. Summary Statistics Insights & Outliers
- **Negative Gross Profit & Margins:** Negative values indicate potential losses, highlighting products or transactions selling below cost or at heavy discounts. Furthermore, Total Sales instances equal to 0 point to obsolete stock that was purchased but strictly remained unsold.
- **High Deviations:** Large variations were observed in Purchase/Actual Prices (distinguishing premium vs. standard products), Freight Costs (suggesting logistics inefficiencies or large bulk shipments), and Stock Turnover (fast-moving vs. indefinitely stagnated inventory).

## 4. Vendor Performance Analysis

### 4.1. Sales & Vendor Output Performance
**Q: Which vendors and brands demonstrate the highest sales performance?**
Analysis reveals top-heavy sales performance. **Diageo North America Inc** overwhelmingly leads vendors with $67.99M in sales, followed by Martignetti Companies at $39.33M. Among the diverse brands, **Jack Daniels No 7 Black** ($7.96M) and Tito's Handmade Vodka heavily drive revenue.

![Count Plots - Vendor and Description](images/Screenshot%202026-03-06%20224147.png)
![Top 10 Vendors and Brands by Sales](images/Screenshot%202026-03-06%20224315.png)

### 4.2. Vendor Purchase Contributions
**Q: Which vendors contribute the most to total purchase dollars, and how much is procurement dependent on these top vendors?**
Procurement is vastly dependent on the top 10 vendors, which collectively make up **65.69%** of the total purchase contribution.

![Pareto Chart - Vendor Contribution](images/Screenshot%202026-03-06%20224335.png)
![Donut Chart - Top 10 Vendor Purchase Contribution](images/Screenshot%202026-03-06%20224349.png)

### 4.3. The Massive Impact of Bulk Purchasing
**Q: Does purchasing in bulk reduce the unit price, and what is the optimal purchase volume?**
Yes. Vendors buying in bulk (categorized exactly as "Large" Order Size) secure the lowest average unit price of roughly $10.78 per unit. This translates to an expansive **~72% reduction in unit cost** compared to Small orders. These bulk pricing strategies successfully incentivize larger volume purchases, elevating overall margin potential.

![Impact of Bulk Purchasing](images/Screenshot%202026-03-06%20224404.png)

### 4.4. Locked Capital
**Q: How much capital is locked in unsold inventory per vendor?**
An enormous total of **$2.71M** remains locked in unsold inventory. Carefully monitoring and scaling down procurement volume from highly-locked top-volume vendors is a critical necessity to free dynamic working capital.

### 4.5. Correlation Insights & Pricing Adjustments
A robust correlation (0.999) between Total Purchase Quantity and Total Sales Quantity proves generally successful and efficient inventory turnover. Conversely, a negative correlation exists between Profit Margin and Total Sales Price (-0.179), heavily implying harsh competitive pricing pressures at scale.

![Correlation Heatmap](images/Screenshot%202026-03-06%20224220.png)

To dynamically optimize operations, we isolated specific brands exhibiting lower sales performance but generating high potential profit margins. These target brands inherently require robust promotional scaling or immediate pricing adjustments.

![Brands for Promotional or Pricing Adjustments](images/Screenshot%202026-03-06%20224240.png)

## 5. Statistical Inference: Profit Margins

**Q: Is there a significant difference in profit margins between top-performing and low-performing vendors?**

### 5.1 Confidence Intervals
- **Top-Performing Vendors (95% CI):** 30.74% to 31.61%
- **Low-Performing Vendors (95% CI):** 40.48% to 42.62%
Notably, low-performing vendors based strictly on sales consistently maintain significantly wider and higher profit margins. 

### 5.2 Hypothesis Testing & Real-World Recommendations
- **Results:** Testing revealed a T-Statistic of -17.6440 and a P-Value of 0.0000. Under this testing, the null hypothesis is cleanly rejected; the variance is statistically significant.
- **For High-Performing Vendors:** Consider exploring precise fractional price adjustments, robust cost/freight optimizations, and bundling strategies to steadily increase currently thin top-tier margins.
- **For Low-Performing Vendors:** Broad, sustained high margins alongside low volume suggests an immediate overriding need for improved targeted marketing, competitive volume pricing, or broader distribution logistics to aggressively scale up operations.

![Confidence Interval Comparison](images/Screenshot%202026-03-06%20224433.png)

## 6. Conclusion
The comprehensive analysis of the existing datasets reveals a powerful, heavily optimized data ingestion pipeline and outlines actionable, statistically baked intelligence regarding vendor health and performance. Stakeholders have empirical backing to adjust purchasing procedures—tightly balancing the scale and reliability of top vendors strictly against cultivating the superior profit margins of lower-volume vendors.
