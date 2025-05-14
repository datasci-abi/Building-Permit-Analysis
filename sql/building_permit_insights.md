# 🧠 Building Permit SQL Insights Report (March 2025)

This report summarizes insights derived from SQL queries on the March 2025 U.S. residential building permit dataset. The data was loaded into a SQLite database and queried using standard SQL techniques to extract meaningful patterns.

---

## 🏆 Top 10 States by Permits Issued

```sql
SELECT State, Total
FROM permits
ORDER BY Total DESC
LIMIT 10;
✅ Shows the 10 states with the highest number of residential building permits issued. Useful for identifying high-growth regions.

💤 Bottom 5 States by Permits Issued
sql
SELECT State, Total
FROM permits
ORDER BY Total ASC
LIMIT 5;
🔻 Highlights states with the least construction activity, which could be seasonal, economic, or population-related.

📊 Share of Total National Permits
sql
SELECT State,
       ROUND(Total * 100.0 / (SELECT SUM(Total) FROM permits), 2) AS Share_Pct
FROM permits
ORDER BY Share_Pct DESC
LIMIT 10;
📈 Calculates what percentage of total U.S. permits each state issued — great for benchmarking.

🧮 Total Permits Nationwide
sql
SELECT SUM(Total) AS national_total FROM permits;
🧾 Gives the total number of units permitted across all U.S. states in March 2025 — useful for framing the rest of the analysis.

💡 Summary
These queries demonstrate how structured data and basic SQL can be used to draw insights from raw government data. This mirrors the type of work done by companies like LightBox, where analytics drive real estate intelligence and decision-making.

✅ Techniques used:

ORDER BY

LIMIT

AGGREGATION (SUM, ROUND)

Subqueries for benchmarks