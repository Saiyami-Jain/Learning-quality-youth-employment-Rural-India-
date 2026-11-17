
import pandas as pd
from scipy.stats import pearsonr

df = pd.read_csv(r"D:\work\1st research project\final_merged_data.csv")

outcomes = [
    "Rural_Male_WPR", "Rural_Female_WPR", "Rural_Person_WPR",
    "Rural_Male_LFPR", "Rural_Female_LFPR", "Rural_Person_LFPR",
    "Rural_Male_UR", "Rural_Female_UR", "Rural_Person_UR",
]

rows = []
for col in outcomes:
    r, p = pearsonr(df["Applied_Reading_%"], df[col])
    rows.append({"Outcome": col, "r": round(r, 3), "p_value": round(p, 3)})

results = pd.DataFrame(rows)
print(results)
results.to_csv(r"D:\work\1st research project\correlation_results.csv", index=False)



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

folder = r"D:\work\1st research project"
df = pd.read_csv(folder + r"\final_merged_data.csv")
res = pd.read_csv(folder + r"\correlation_results.csv")

# Chart 1: main result, Applied Reading vs Rural Person WPR
x = df["Applied_Reading_%"]
y = df["Rural_Person_WPR"]
slope, intercept = np.polyfit(x, y, 1)
xs = np.linspace(x.min(), x.max(), 100)

fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(x, y, color="#1f4e79")
ax.plot(xs, slope * xs + intercept, color="#c0392b")

# label the three highest and three lowest states on applied reading
extremes = pd.concat([df.nlargest(3, "Applied_Reading_%"),
                      df.nsmallest(3, "Applied_Reading_%")])
for _, row in extremes.iterrows():
    ax.annotate(row["State"], (row["Applied_Reading_%"], row["Rural_Person_WPR"]),
                textcoords="offset points", xytext=(5, 5), fontsize=8)

ax.set_xlabel("Applied reading, rural youth aged 14-18 (%)")
ax.set_ylabel("Rural WPR, youth aged 15-29 (%)")
ax.set_title("Applied reading vs rural worker population ratio (26 states, r = -0.54, p = 0.004)")
plt.tight_layout()
plt.savefig(folder + r"\chart1_scatter_wpr.png", dpi=200)
plt.show()

# Chart 2: all nine correlations
fig, ax = plt.subplots(figsize=(8, 6))
colors = ["#1f4e79" if p < 0.05 else "#aaaaaa" for p in res["p_value"]]
ax.barh(res["Outcome"], res["r"], color=colors)
ax.axvline(0, color="black", linewidth=0.8)
ax.invert_yaxis()
ax.set_xlabel("Correlation with Applied_Reading_% (r)")
ax.set_title("Nine correlations (blue = p below 0.05, grey = not)")
plt.tight_layout()
plt.savefig(folder + r"\chart2_all_correlations.png", dpi=200)
plt.show()




import pandas as pd

df = pd.read_csv(r"D:\work\1st research project\final_merged_data.csv")
full = df["Applied_Reading_%"].corr(df["Rural_Person_WPR"])
print("All 26 states:", round(full, 3))

without_kerala = df[df["State"] != "Kerala"]
print("Without Kerala:", round(without_kerala["Applied_Reading_%"].corr(without_kerala["Rural_Person_WPR"]), 3))

rs = {}
for state in df["State"]:
    d = df[df["State"] != state]
    rs[state] = d["Applied_Reading_%"].corr(d["Rural_Person_WPR"])
rs = pd.Series(rs)
print("Weakest result when dropping one state:", rs.idxmax(), round(rs.max(), 3))
print("Strongest result when dropping one state:", rs.idxmin(), round(rs.min(), 3))

print(df.nsmallest(3, "Rural_Person_WPR")[["State", "Applied_Reading_%", "Rural_Person_WPR"]])




from scipy.stats import pearsonr
import pandas as pd
df = pd.read_csv(r"D:\work\1st research project\final_merged_data.csv")
d = df[df["State"] != "Kerala"]
print(pearsonr(d["Applied_Reading_%"], d["Rural_Person_WPR"]))