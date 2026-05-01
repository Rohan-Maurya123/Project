from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    df = df.copy()

    # Scale Amount
    scaler = StandardScaler()
    df['Amount'] = scaler.fit_transform(df[['Amount']])

    # Drop Time
    df = df.drop(['Time'], axis=1)

    X = df.drop('Class', axis=1)
    y = df['Class']

    return X, y