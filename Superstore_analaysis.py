import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# ============================================================
# 1. CREATE OUTPUT FOLDER
# ============================================================

OUTPUT_DIR = "output"
CLEANED_DATA_DIR = "cleaned_data"
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(CLEANED_DATA_DIR, exist_ok=True)


# ============================================================
# 2. LOAD DATASET
# ============================================================

df = pd.read_csv(
    r"C:\Users\user\Desktop\Python\Project\Superstore_analysis\Superstore_data.csv",
    encoding="latin1"
)


# ============================================================
# PROJECT TITLE
# ============================================================

print("=" * 60)
print("SUPER STORE ANALYSIS")
print("=" * 60)


# ============================================================
# 3. EXPLORE DATA
# ============================================================

def explore_data(df):

    print("\nNumber of Rows and Columns:")
    print(df.shape)

    print("\nName of the columns:")
    print(df.columns)

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nLast 5 rows:")
    print(df.tail())

    print("\nDetailed Information of data:")
    df.info()

    print("\nStatistical view of data:")
    print(df.describe())

    print("\nNumber of Missing values:")
    print(df.isnull().sum())

    print("\nNumber of Duplicate rows:")
    print(df.duplicated().sum())


# ============================================================
# 4. DATA QUALITY CHECK
# ============================================================

def data_quality_check(df):

    print("\nCategories:")
    print(df["Category"].unique())
    print(df["Category"].value_counts())

    print("\nSubcategories:")
    print(df["Sub-Category"].unique())
    print(df["Sub-Category"].value_counts())

    print("\nShip Mode:")
    print(df["Ship Mode"].unique())
    print(df["Ship Mode"].value_counts())
    print(df["Ship Mode"].value_counts().sum())

    print("\nCountry:")
    print(df["Country"].unique())

    print("\nRegion:")
    print(df["Region"].unique())
    print(df["Region"].value_counts())

    print("\nSegment:")
    print(df["Segment"].unique())
    print(df["Segment"].value_counts())
    print(df["Segment"].value_counts().sum())

    print("\nAre any orders shipped before they were ordered?")
    print((df["Order Date"] > df["Ship Date"]).sum())

    print("\nAny negative or zero values in sales?")
    print((df["Sales"] <= 0).sum())

    print("\nAny negative or zero in quantity?")
    print((df["Quantity"] <= 0).sum())

    print("\nAny loss in profit?")
    print((df["Profit"] < 0).sum())

    print("\nAny impossible or unusual values in discount?")
    print(df["Discount"].unique())
    print(df["Discount"].value_counts())


"""
Data quality check conclusion:

The dataset contains no missing values or duplicate rows.
Date fields were converted to datetime format, and no invalid
order/ship date relationships were found.

Sales and Quantity contain no zero or negative values.
Negative Profit values were identified as potential business
losses rather than automatically treated as data-quality errors.
"""


# ============================================================
# 5. BUSINESS ANALYSIS
# ============================================================

def business_analysis(df):

    print("\nTotal Sales")
    print(df["Sales"].sum())

    print("\nTotal Quantity")
    print(df["Quantity"].sum())

    print("\nTotal Profit")
    print(df["Profit"].sum())

    print("\nThe Number of orders")
    print(df["Order ID"].nunique())

    print("\nThe Number of customers")
    print(df["Customer ID"].nunique())


"""
Overall summary:

Total Sales         : 2297200.8603
Total Quantity      : 37873
Total Profit        : 286397.0217
Number of Orders    : 5009
Number of Customers : 793
"""


# ============================================================
# 6. CATEGORY ANALYSIS
# ============================================================

def category_analysis(df):

    print("\nWhich category has the highest Sales?")

    Category_vs_sales = pd.pivot_table(
        df,
        values="Sales",
        index="Category",
        aggfunc="sum"
    )

    print(Category_vs_sales)

    print("Highest sales in category is Technology : 836154.0330")


    print("\nWhich category has the highest Profit?")

    Category_vs_profit = pd.pivot_table(
        df,
        values="Profit",
        index="Category",
        aggfunc="sum"
    )

    print(Category_vs_profit)

    print("Highest Profit in category is Technology : 145454.9481")


    print("\nWhich category has the highest Quantity?")

    Category_vs_Quantity = pd.pivot_table(
        df,
        values="Quantity",
        index="Category",
        aggfunc="sum"
    )

    print(Category_vs_Quantity)

    print("Highest Quantity in category is Office Supplies: 22906")


    print("\nIs the highest-Sales category also the highest-Profit category?")

    print("\nComparison")

    print(
        "\nHighest Sales category is Technology : 836154.0330"
        "\nHighest Profit category is Technology : 145454.9481"
    )

    print("Are they same? Yes, both are the same category Technology")


    print("\nAverage sales in category")
    print(df.groupby("Category")["Sales"].mean())


    print("\nAverage Profit in category")
    print(df.groupby("Category")["Profit"].mean())


    return Category_vs_sales


# ============================================================
# 7. SUB-CATEGORY ANALYSIS
# ============================================================

def Sub_Category_Analysis(df):

    print("\nTop 5 sub-categories by Sales")

    Top_Sales = pd.pivot_table(
        df,
        values="Sales",
        index="Sub-Category",
        aggfunc="sum"
    )

    descending_sales = Top_Sales.sort_values(
        by="Sales",
        ascending=False
    )

    print(descending_sales.head())


    print("\nBottom 5 sub-categories by Sales")
    print(descending_sales.tail())


    print("\nTop 5 sub-categories by Profit")

    Top_Profit = pd.pivot_table(
        df,
        values="Profit",
        index="Sub-Category",
        aggfunc="sum"
    )

    descending_Profit = Top_Profit.sort_values(
        by="Profit",
        ascending=False
    )

    print(descending_Profit.head())


    print("\nBottom 5 sub-categories by Profit")
    print(descending_Profit.tail())


    print("\nInvestigate whether high Sales can coexist with low or negative Profit.")

    print(
        "Answer: Yes, Tables ranks 4th in Sales among the "
        "sub-categories, generating 206,965.532 in Sales. "
        "However, it generated a negative Profit of -17,725.4811. "
        "This indicates that high Sales can coexist with negative "
        "Profit and that revenue alone does not guarantee profitability."
    )


# ============================================================
# 8. GEOGRAPHIC ANALYSIS
# ============================================================

def Geographic_Analysis(df):

    print("\nRegion-wise Sales")

    region_sales = df.groupby("Region")["Sales"].sum()
    print(region_sales)


    print("\nRegion-wise Profit")

    region_profit = df.groupby("Region")["Profit"].sum()
    print(region_profit.sort_values())


    print("\nState-wise Sales")
    print(df.groupby("State")["Sales"].sum())


    print("\nState-wise Profit")

    State_profit = df.groupby("State")["Profit"].sum()
    print(State_profit.sort_values())


    print("\nCity-wise Sales")

    City_sales = df.groupby("City")["Sales"].sum()
    print(City_sales)


    print("\nCity-wise Profit")

    City_profit = df.groupby("City")["Profit"].sum()
    print(City_profit.sort_values())


    print("\nIdentify the strongest region")
    print("Answer: West. Because sales and profit is high")


    print("\nIdentify weak or loss-making geographic areas")
    print("\nCity: Philadelphia")
    print("State: Texas")


    print("\nIdentify high-contribution cities")

    print("\nHighest City sales")

    city_sales_ascending = City_sales.sort_values(
        ascending=False
    )

    print(city_sales_ascending.head())


    print("\nHighest City Profit")

    city_profit_ascending = City_profit.sort_values(
        ascending=False
    )

    print(city_profit_ascending.head())


    return region_sales


# ============================================================
# 9. TIME ANALYSIS
# ============================================================

def Time_Analysis(df):

    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])


    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month
    df["Month_name"] = df["Order Date"].dt.month_name()
    df["Day"] = df["Order Date"].dt.day
    df["Day_name"] = df["Order Date"].dt.day_name()


    print("\nCalculate year-wise Sales and Profit:")

    year_sales = pd.pivot_table(
        df,
        values="Sales",
        index="Year",
        aggfunc="sum"
    )

    print("Year-wise Sales:\n", year_sales)


    year_Profit = pd.pivot_table(
        df,
        values="Profit",
        index="Year",
        aggfunc="sum"
    )

    print("Year-wise Profit:\n", year_Profit)


    print("\nCalculate month-wise Sales and Profit")

    month_sales = pd.pivot_table(
        df,
        values="Sales",
        index="Month_name",
        aggfunc="sum"
    )

    print("Month-wise Sales:\n", month_sales)


    month_Profit = pd.pivot_table(
        df,
        values="Profit",
        index="Month_name",
        aggfunc="sum"
    )

    print("Month-wise Profit:\n", month_Profit)


    print("\nHighest-Sales month and highest-Profit month:")

    high_month_sales = month_sales.sort_values(
        by="Sales",
        ascending=False
    )

    print("Highest-sales month:", high_month_sales.head())


    high_month_profit = month_Profit.sort_values(
        by="Profit",
        ascending=False
    )

    print("Highest-Profit month:", high_month_profit.head())


    print(
        "Answer: Highest Sales Month: November 352461.0710"
        "\nHighest Profit Month: December 43369.1919"
    )


    print("\nCompare Sales growth with Profit growth")

    print("Sales Growth")
    print(year_sales.pct_change() * 100)

    print("Profit Growth")
    print(year_Profit.pct_change() * 100)


    print(
        "Conclusion: In 2015, Sales decreased by 2.83%, while "
        "Profit increased by 24.37%. In 2016, both Sales and "
        "Profit grew strongly, with Profit growth slightly higher "
        "than Sales growth. In 2017, Sales continued to grow by "
        "20.36%, but Profit grew by only 14.24%. This shows that "
        "Sales growth and Profit growth did not always move at "
        "the same rate."
    )


    return year_sales


# ============================================================
# 10. CUSTOMER ANALYSIS
# ============================================================

def customer_analysis(df):

    print("\nIdentify top customers by Sales")

    customer_sales = pd.pivot_table(
        df,
        values="Sales",
        index="Customer Name",
        aggfunc="sum"
    )

    Top_customer_sales = customer_sales.sort_values(
        by="Sales",
        ascending=False
    )

    print(Top_customer_sales.head(10))


    print("\nIdentify top customers by Profit")

    customer_Profit = pd.pivot_table(
        df,
        values="Profit",
        index="Customer Name",
        aggfunc="sum"
    )

    Top_customer_Profit = customer_Profit.sort_values(
        by="Profit",
        ascending=False
    )

    print(Top_customer_Profit.head(10))


    print("\nCompare high-Sales customers with high-Profit customers")

    print(
        "Answer: Six customers appear in both the Top 10 Sales "
        "and Top 10 Profit lists, indicating that these customers "
        "contribute strongly to both sales and profitability."
    )


    Top_10_sales = Top_customer_sales.head(10)["Sales"].sum()

    print("Top_10_sales:", Top_10_sales)


    Top_sales = df["Sales"].sum()

    print("Top_sales:", Top_sales)


    customer_concentration = (Top_10_sales / Top_sales) * 100

    print("Top 10 customer sales percentage:", customer_concentration)


    print("\nDetermine customer concentration if meaningful")

    print(
        "Answer: The Top 10 customers contribute approximately "
        "6.70% of total Sales, indicating relatively low customer "
        "concentration. This suggests that the business is not heavily "
        "dependent on a small group of customers."
    )


# ============================================================
# 11. PRODUCT ANALYSIS
# ============================================================

def product_analysis(df):

    print("\nTop 10 products by Sales")

    Product_sales = pd.pivot_table(
        df,
        values="Sales",
        index="Product Name",
        aggfunc="sum"
    )

    Top_product_sales = Product_sales.sort_values(
        by="Sales",
        ascending=False
    )

    print(Top_product_sales.head(10))


    print("\nTop 10 products by Profit")

    Product_profit = pd.pivot_table(
        df,
        values="Profit",
        index="Product Name",
        aggfunc="sum"
    )

    Top_product_profit = Product_profit.sort_values(
        by="Profit",
        ascending=False
    )

    print(Top_product_profit.head(10))


    print("\nBottom 10 products by Profit")

    bottom_product_profit = Product_profit.sort_values("Profit")

    print(bottom_product_profit.head(10))


    print("\nIdentify products generating losses")

    loss_making_products = Product_profit[
        Product_profit["Profit"] < 0
    ]

    print(loss_making_products)


    print("\nLook for products with high Sales but weak Profit")

    High_sales_weak_profit = pd.pivot_table(
        df,
        values=["Sales", "Profit"],
        index="Product Name",
        aggfunc="sum"
    )

    loss_products = High_sales_weak_profit[
        High_sales_weak_profit["Profit"] < 0
    ]

    print(loss_products)


    sort_sales_profit = loss_products.sort_values(
        by=["Sales", "Profit"],
        ascending=[False, True]
    )

    print(sort_sales_profit)


# ============================================================
# 12. VISUALIZATION
# ============================================================

def visualization(year_sales, Category_vs_sales, region_sales):

    print("\nHow are Sales changing over time?")

    plt.figure(figsize=(8, 5))

    plt.plot(
        year_sales.index,
        year_sales["Sales"],
        color="blue",
        marker="D",
        linestyle="-",
        label="Sales",
        markersize=8,
        linewidth=3
    )

    plt.title("Sales Over Time")
    plt.xlabel("Year")
    plt.ylabel("Sales")
    plt.legend()
    plt.grid()
    plt.tight_layout()

    plt.savefig(
        os.path.join(OUTPUT_DIR, "sales_over_time.png")
    )
    plt.show()
    plt.close()


    # --------------------------------------------------

    print("\nWhich category has the highest Sales?")

    plt.figure(figsize=(7, 5))

    plt.bar(
        Category_vs_sales.index,
        Category_vs_sales["Sales"],
        width=0.5,
        color="red",
        edgecolor="black"
    )

    plt.title("Category-wise Sales")
    plt.xlabel("Category")
    plt.ylabel("Sales")
    plt.grid(axis="y")
    plt.tight_layout()

    plt.savefig(
        os.path.join(OUTPUT_DIR, "category_sales.png")
    )
    plt.show()
    plt.close()


    # --------------------------------------------------

    print("\nWhich region contributes most?")

    plt.figure(figsize=(7, 5))

    plt.barh(
        region_sales.index,
        region_sales.values,
        height=0.5,
        color="pink",
        edgecolor="black"
    )

    plt.title("Region-wise Sales")
    plt.xlabel("Sales")
    plt.ylabel("Region")
    plt.grid(axis="x")
    plt.tight_layout()

    plt.savefig(
        os.path.join(OUTPUT_DIR, "region_sales.png")
    )
    plt.show()
    plt.close()


    # --------------------------------------------------

    print("\nHow are Sales values distributed?")

    plt.figure(figsize=(8, 5))

    plt.hist(
        df["Sales"],
        bins=10,
        color="green",
        edgecolor="black"
    )

    plt.title("Sales Distribution")
    plt.xlabel("Sales")
    plt.ylabel("Frequency")
    plt.grid(axis="y")
    plt.tight_layout()

    plt.savefig(
        os.path.join(OUTPUT_DIR, "sales_distribution.png")
    )
    plt.show()
    plt.close()


    # --------------------------------------------------

    print("\nAre there unusual Sales or Profit values?")

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)

    box = plt.boxplot(
        df["Sales"],
        patch_artist=True
    )

    box["boxes"][0].set_facecolor("green")

    plt.title("Sales Distribution")
    plt.ylabel("Sales")
    plt.grid(axis="y")


    plt.subplot(1, 2, 2)

    boxs = plt.boxplot(
        df["Profit"],
        patch_artist=True
    )

    boxs["boxes"][0].set_facecolor("green")

    plt.title("Profit Distribution")
    plt.ylabel("Profit")
    plt.grid(axis="y")

    plt.tight_layout()

    plt.savefig(
        os.path.join(OUTPUT_DIR, "sales_profit_boxplot.png")
    )
    plt.show()
    plt.close()


    # --------------------------------------------------

    print("\nWhich category has the most orders?")

    plt.figure(figsize=(7, 5))

    sns.countplot(
        x=df["Category"],
        hue=df["Category"],
        palette="Set3",
        edgecolor="black",
        legend=False
    )

    plt.title("Category-wise Orders Count")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.tight_layout()

    plt.savefig(
        os.path.join(OUTPUT_DIR, "category_orders.png")
    )
    plt.show()
    plt.close()


    # --------------------------------------------------

    print("\nWhat is the relationship between Sales and Profit?")

    plt.figure(figsize=(8, 5))

    sns.scatterplot(
        x=df["Sales"],
        y=df["Profit"],
        color="brown",
        marker="*"
    )

    plt.title("Relationship Between Sales and Profit")
    plt.xlabel("Sales")
    plt.ylabel("Profit")
    plt.grid()
    plt.tight_layout()

    plt.savefig(
        os.path.join(OUTPUT_DIR, "sales_profit_relationship.png")
    )
    plt.show()
    plt.close()


    # --------------------------------------------------

    print("\nHow are important numerical variables correlated?")

    numeric_df = df[
        ["Sales", "Quantity", "Discount", "Profit"]
    ]

    corr = numeric_df.corr()

    plt.figure(figsize=(8, 6))

    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        linewidth=1,
        linecolor="black",
        fmt=".2f"
    )

    plt.title("Correlation Heatmap")
    plt.tight_layout()

    plt.savefig(
        os.path.join(OUTPUT_DIR, "correlation_heatmap.png")
    )
    plt.show()
    plt.close()


    # --------------------------------------------------

    print("\nHow do multiple numerical variables relate?")

    pairplot = sns.pairplot(
        numeric_df,
        diag_kind="hist"
    )

    pairplot.fig.suptitle(
        "Relationships Between Numerical Variables",
        y=1.02
    )

    pairplot.savefig(
        os.path.join(OUTPUT_DIR, "numerical_pairplot.png")
    )
    plt.show()
    plt.close("all")


    print("\nAll visualizations have been saved successfully.")

# ============================================================
# 13. BUSINESS INSIGHTS
# ============================================================

def Business_Insights(df):

    print("\n========== BUSINESS INSIGHTS ==========")


    print("\n1. Technology is the strongest category")

    print(
        "Technology generated the highest Sales and Profit "
        "among the three categories."
    )

    print(
        "This indicates that Technology is an important contributor "
        "to overall business performance."
    )


    print("\n2. High Sales do not always mean high Profit")

    print(
        "Phones had the highest Sales among sub-categories, "
        "while Tables recorded a negative Profit."
    )

    print(
        "This shows that revenue alone should not be used to "
        "evaluate business performance."
    )

    print(
        "Profitability should be considered along with Sales."
    )


    print("\n3. West is the strongest region")

    print(
        "The West region generated the highest overall Sales and Profit."
    )

    print(
        "The company can study the strategies used in this region "
        "and identify opportunities to improve weaker regions."
    )


    print("\n4. November has the highest Sales")

    print(
        "November recorded the highest monthly Sales."
    )

    print(
        "This suggests that the business experiences strong demand "
        "during this period."
    )

    print(
        "The company can prepare inventory and marketing campaigns "
        "in advance for high-demand months."
    )


    print("\n5. December has the highest Profit")

    print(
        "December generated the highest monthly Profit."
    )

    print(
        "This indicates that the most profitable period is not "
        "necessarily the same as the highest-sales period."
    )

    print(
        "The company should therefore track both Sales and Profit "
        "when evaluating monthly performance."
    )


    print("\n6. Some high-sales products may have weak profitability")

    print(
        "The product-level analysis identified products with high "
        "Sales but relatively low or negative Profit."
    )

    print(
        "These products should be reviewed for pricing, discount "
        "levels, shipping costs and other expenses."
    )


# ============================================================
# 14. RUN COMPLETE PROJECT
# ============================================================

explore_data(df)

data_quality_check(df)

business_analysis(df)

Category_vs_sales = category_analysis(df)

Sub_Category_Analysis(df)

region_sales = Geographic_Analysis(df)

year_sales = Time_Analysis(df)

customer_analysis(df)

product_analysis(df)

visualization(
    year_sales,
    Category_vs_sales,
    region_sales
)

Business_Insights(df)


# ============================================================
# PROJECT COMPLETED
# ============================================================

print("\n" + "=" * 60)
print("PROJECT COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nAll charts have been saved in the 'output' folder.")

df.to_csv(
    os.path.join(CLEANED_DATA_DIR, "Superstore_cleaned.csv"),
    index=False
)