def detect_anomalies(df, threshold=2):
    """
    Detects anomalies in temperature data based on Z-score.
    Returns the dataframe with an 'Anomaly' column.
    """
    mean = df['Temperature'].mean()
    std = df['Temperature'].std()

    df['Anomaly'] = df['Temperature'].apply(
        lambda x: 1 if abs(x - mean) > threshold * std else 0
    )
    return df