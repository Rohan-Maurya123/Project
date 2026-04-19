def trend_analysis(df, window=12):
    """
    Computes a rolling mean for trend analysis.
    Returns the dataframe with a 'Rolling_Mean' column.
    """
    df['Rolling_Mean'] = df['Temperature'].rolling(window=window).mean()
    return df