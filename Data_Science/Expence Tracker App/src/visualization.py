import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def create_plotly_charts(df, metrics):
    """
    Generates high-tech animated Plotly charts for the AI dashboard.
    """
    # High-Energy Cyberpunk Palette
    NEON_COLORS = ['#00f2ff', '#ff00ff', '#00ff00', '#7000ff', '#ffea00', '#ff5e00']
    
    # 1. Animated Stacked Bar Chart (High Velocity)
    expenses_df = df[df['Type'] == 'Expense'].copy()
    # Ensure chronological order for animation
    expenses_df = expenses_df.sort_values('Date')
    monthly_cat = expenses_df.groupby(['Year_Month', 'Category'])['Amount'].sum().reset_index()
    
    fig_monthly_bar = px.bar(
        monthly_cat,
        x='Category',
        y='Amount',
        color='Category',
        animation_frame='Year_Month',
        title="NEURAL SECTOR ANALYSIS (VELOCITY)",
        template="plotly_dark",
        color_discrete_sequence=NEON_COLORS,
        range_y=[0, monthly_cat['Amount'].max() * 1.1],
        text_auto='.2s'
    )
    
    fig_monthly_bar.update_traces(
        marker=dict(line=dict(width=2, color='rgba(255, 255, 255, 0.2)')),
        hovertemplate="<b>Sector: %{x}</b><br>Value: ₹%{y:,.0f}<extra></extra>"
    )
    
    fig_monthly_bar.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis_title="ACTIVE SECTORS",
        yaxis_title="FLUX INTENSITY (INR)",
        showlegend=False,
        margin=dict(t=80, b=40),
        font=dict(family="Courier New, monospace", color="#00f2ff"),
        # Style the animation buttons
        updatemenus=[dict(
            type="buttons",
            showactive=False,
            x=0.1, y=0,
            buttons=[dict(label="▶ RUN SYSTEM SCAN", method="animate")]
        )]
    )

    # 2. Category Breakdown (Donut HUD Style)
    fig_category = px.pie(
        names=metrics['category_sum'].index,
        values=metrics['category_sum'].values,
        hole=0.7,
        title="SPENDING MATRIX (HUD)",
        template="plotly_dark",
        color_discrete_sequence=NEON_COLORS
    )
    fig_category.update_traces(
        textposition='outside', 
        textinfo='percent+label',
        marker=dict(line=dict(width=2, color='#111')),
        hovertemplate="<b>%{label}</b><br>Intensity: ₹%{value:,.0f}<br>%{percent}<extra></extra>"
    )
    fig_category.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Courier New, monospace", color="#00f2ff")
    )

    # 3. Monthly Trend (Glow Area Chart)
    fig_trend = px.area(
        x=metrics['monthly_trend'].index,
        y=metrics['monthly_trend'].values,
        title="SYSTEM FLUX VELOCITY",
        template="plotly_dark",
        labels={'x': 'TIME CYCLE', 'y': 'FLUX'},
        color_discrete_sequence=['#00f2ff']
    )
    fig_trend.update_layout(
        plot_bgcolor="rgba(0,0,0,0)", 
        paper_bgcolor="rgba(0,0,0,0)",
        hovermode="x unified",
        font=dict(family="Courier New, monospace", color="#00f2ff")
    )
    fig_trend.update_traces(
        fillcolor='rgba(0, 242, 255, 0.15)',
        line=dict(width=4, color='#00f2ff', shape='spline'),
        hovertemplate="FLUX: ₹%{y:,.0f}<extra></extra>"
    )

    # 4. Daily Spending Flow (Neural Signal Line)
    daily_spending = df[df['Type'] == 'Expense'].groupby('Date')['Amount'].sum().reset_index()
    fig_daily = px.line(
        daily_spending,
        x='Date',
        y='Amount',
        title="DAILY SIGNAL INTENSITY",
        template="plotly_dark",
        line_shape='spline',
        color_discrete_sequence=['#ff00ff']
    )
    fig_daily.update_layout(
        plot_bgcolor="rgba(0,0,0,0)", 
        paper_bgcolor="rgba(0,0,0,0)",
        hovermode="x unified",
        font=dict(family="Courier New, monospace", color="#ff00ff")
    )
    fig_daily.update_traces(
        line=dict(width=3, color='#ff00ff'),
        hovertemplate="SIGNAL: ₹%{y:,.0f}<extra></extra>"
    )

    return fig_category, fig_trend, fig_daily, fig_monthly_bar