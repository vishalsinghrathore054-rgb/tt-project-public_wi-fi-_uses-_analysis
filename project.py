import pandas as pd, numpy as np, matplotlib.pyplot as plt

np.random.seed(1)


df = pd.DataFrame({
    "Location": np.random.choice(
        ["Railway Station","Bus Stand","Park","Mall","Airport"],100),
    "Data_Used_MB": np.random.randint(100,5000,100),
    "Avg_Speed_Mbps": np.random.randint(5,50,100)
})


df["Location"].value_counts().plot(kind="bar", title="Users per Location")
plt.show()


df["Data_Used_MB"].plot(kind="hist", bins=10, title="Data Usage")
plt.show()


df.groupby("Location")["Avg_Speed_Mbps"].mean().plot(kind="line", marker='o',
title="Avg Speed")
plt.show()
