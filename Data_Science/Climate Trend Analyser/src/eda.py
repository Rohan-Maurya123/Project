import matplotlib.pyplot as plt

def plot_temperature(df):
    plt.figure()
    plt.plot(df['Date'], df['Temperature'])
    plt.title("Temperature Over Time")
    plt.xlabel("Date")
    plt.ylabel("Temperature")
    plt.savefig("outputs/plots/temp_trend.png")
    plt.close()