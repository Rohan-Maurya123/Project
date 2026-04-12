def create_labels(df):
    max_cycle = df.groupby('unit')['cycle'].max().reset_index()
    max_cycle.columns = ['unit', 'max_cycle']

    df = df.merge(max_cycle, on='unit')
    df['RUL'] = df['max_cycle'] - df['cycle']
    df['failure'] = df['RUL'].apply(lambda x: 1 if x < 30 else 0)

    print("Labels Created")
    return df


def prepare_features(df):
    from sklearn.model_selection import train_test_split

    sensor_cols = [col for col in df.columns if 'sensor' in col]

    X = df[sensor_cols]
    y = df['failure']

    return train_test_split(X, y, test_size=0.2, random_state=42)