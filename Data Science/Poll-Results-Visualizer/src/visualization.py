import altair as alt
import pandas as pd

def plot_interactive_bar(data, x_label, y_label, title):
    """Generates an interactive Altair bar chart."""
    if isinstance(data, pd.Series):
        df_plot = data.reset_index()
        df_plot.columns = [x_label, y_label]
    else:
        df_plot = data.reset_index()
        # Handle crosstab data which might have multiple columns
        df_plot = df_plot.melt(id_vars=df_plot.columns[0], var_name='Response', value_name='Count')
        x_label = df_plot.columns[0]
        y_label = 'Count'

    chart = alt.Chart(df_plot).mark_bar().encode(
        x=alt.X(f'{x_label}:N', title=x_label, sort='-y'),
        y=alt.Y(f'{y_label}:Q', title=y_label),
        color=alt.Color(f'{x_label}:N', legend=None),
        tooltip=[x_label, y_label]
    ).properties(
        title=title,
        width='container',
        height=400
    ).interactive()
    
    return chart

def plot_stacked_bar(data, x_label, title):
    """Generates an interactive Altair stacked bar chart."""
    df_plot = data.reset_index()
    df_plot = df_plot.melt(id_vars=df_plot.columns[0], var_name='Response', value_name='Count')
    category_col = df_plot.columns[0]

    chart = alt.Chart(df_plot).mark_bar().encode(
        x=alt.X(f'{category_col}:N', title=category_col),
        y=alt.Y('sum(Count):Q', title='Count'),
        color='Response:N',
        tooltip=[category_col, 'Response', 'Count']
    ).properties(
        title=title,
        width='container',
        height=400
    ).interactive()

    return chart