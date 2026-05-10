import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Personal Expense Tracker",
    page_icon="💰",
    layout="wide"
)

# ==========================================
# LOAD DATA
# ==========================================

DATA_PATH = "data/expenses.csv"

df = pd.read_csv(DATA_PATH)

df["Date"] = pd.to_datetime(df["Date"])

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("💳 Expense Manager")

# ==========================================
# ADD NEW EXPENSE
# ==========================================

st.sidebar.header("➕ Add New Expense")

expense_date = st.sidebar.date_input("Expense Date")

expense_category = st.sidebar.selectbox(
    "Category",
    [
        "Food",
        "Transport",
        "Shopping",
        "Entertainment",
        "Bills",
        "Healthcare"
    ]
)

expense_amount = st.sidebar.number_input(
    "Amount",
    min_value=1.0,
    step=10.0
)

payment_method = st.sidebar.selectbox(
    "Payment Method",
    [
        "Cash",
        "UPI",
        "Credit Card",
        "Debit Card"
    ]
)

expense_description = st.sidebar.text_input(
    "Description"
)

if st.sidebar.button("Add Expense"):

    new_expense = pd.DataFrame({
        "Date": [expense_date],
        "Category": [expense_category],
        "Amount": [expense_amount],
        "Payment_Method": [payment_method],
        "Description": [expense_description]
    })

    new_expense.to_csv(
        DATA_PATH,
        mode="a",
        header=False,
        index=False
    )

    st.sidebar.success("Expense Added Successfully!")

    st.rerun()

# ==========================================
# FILTERS
# ==========================================

st.sidebar.header("📌 Filters")

selected_category = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

selected_payment = st.sidebar.multiselect(
    "Payment Method",
    options=df["Payment_Method"].unique(),
    default=df["Payment_Method"].unique()
)

filtered_df = df[
    (df["Category"].isin(selected_category)) &
    (df["Payment_Method"].isin(selected_payment))
]

# ==========================================
# TITLE
# ==========================================

st.title("💰 Personal Expense Tracker Dashboard")

st.markdown(
    "Track, Analyze, and Visualize Personal Expenses in Real-Time"
)

# ==========================================
# KPI METRICS
# ==========================================

total_spending = filtered_df["Amount"].sum()

average_spending = filtered_df["Amount"].mean()

highest_category = (
    filtered_df.groupby("Category")["Amount"]
    .sum()
    .idxmax()
)

total_transactions = len(filtered_df)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "💸 Total Spending",
    f"₹{total_spending:,.2f}"
)

col2.metric(
    "📊 Average Expense",
    f"₹{average_spending:,.2f}"
)

col3.metric(
    "🏆 Top Category",
    highest_category
)

col4.metric(
    "🧾 Total Transactions",
    total_transactions
)

st.divider()

# ==========================================
# TABS
# ==========================================

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Dashboard",
    "📈 Analytics",
    "🧾 Expense Records",
    "📅 Monthly Insights",
    "📥 Download Reports"
])

# ==========================================
# TAB 1 - DASHBOARD
# ==========================================

with tab1:

    st.subheader("📊 Expense Overview")

    col1, col2 = st.columns(2)

    # CATEGORY BAR CHART
    with col1:

        category_data = (
            filtered_df.groupby("Category")["Amount"]
            .sum()
            .reset_index()
        )

        category_chart = px.bar(
            category_data,
            x="Category",
            y="Amount",
            title="Category Wise Spending",
            text_auto=True
        )

        st.plotly_chart(
            category_chart,
            use_container_width=True
        )

    # PAYMENT PIE CHART
    with col2:

        payment_chart = px.pie(
            filtered_df,
            names="Payment_Method",
            values="Amount",
            title="Payment Method Analysis"
        )

        st.plotly_chart(
            payment_chart,
            use_container_width=True
        )

    # DAILY TREND
    daily_data = (
        filtered_df.groupby("Date")["Amount"]
        .sum()
        .reset_index()
    )

    daily_chart = px.area(
        daily_data,
        x="Date",
        y="Amount",
        title="Daily Spending Trend"
    )

    st.plotly_chart(
        daily_chart,
        use_container_width=True
    )

# ==========================================
# TAB 2 - ANALYTICS
# ==========================================

with tab2:

    st.subheader("📈 Expense Analytics")

    # MONTHLY TREND
    filtered_df["Month"] = (
        filtered_df["Date"]
        .dt.strftime("%b")
    )

    monthly_data = (
        filtered_df.groupby("Month")["Amount"]
        .sum()
        .reset_index()
    )

    monthly_chart = px.line(
        monthly_data,
        x="Month",
        y="Amount",
        markers=True,
        title="Monthly Spending Trend"
    )

    st.plotly_chart(
        monthly_chart,
        use_container_width=True
    )

    # CATEGORY DISTRIBUTION
    treemap = px.treemap(
        filtered_df,
        path=["Category"],
        values="Amount",
        title="Expense Distribution Treemap"
    )

    st.plotly_chart(
        treemap,
        use_container_width=True
    )

# ==========================================
# TAB 3 - EXPENSE RECORDS
# ==========================================

with tab3:

    st.subheader("🧾 Expense Records")

    st.dataframe(
        filtered_df.sort_values(
            by="Date",
            ascending=False
        ),
        use_container_width=True
    )

# ==========================================
# TAB 4 - MONTHLY INSIGHTS
# ==========================================

with tab4:

    st.subheader("📅 Financial Insights")

    highest_expense = filtered_df.loc[
        filtered_df["Amount"].idxmax()
    ]

    st.success(
        f"Highest Expense: ₹{highest_expense['Amount']:,.2f}"
    )

    st.info(
        f"Highest Spending Category: {highest_category}"
    )

    st.warning(
        f"Average Daily Spending: ₹{average_spending:,.2f}"
    )

    # CATEGORY SUMMARY
    summary = (
        filtered_df.groupby("Category")["Amount"]
        .agg(["sum", "mean", "count"])
        .reset_index()
    )

    st.subheader("📌 Category Summary")

    st.dataframe(
        summary,
        use_container_width=True
    )

# ==========================================
# TAB 5 - DOWNLOAD REPORTS
# ==========================================

with tab5:

    st.subheader("📥 Download Expense Report")

    csv = filtered_df.to_csv(index=False)

    st.download_button(
        label="⬇ Download CSV Report",
        data=csv,
        file_name="expense_report.csv",
        mime="text/csv"
    )

    st.success("Generate reports for analysis and sharing.")

# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "Built with Python, Streamlit, Pandas, and Plotly"
)