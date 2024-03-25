from scipy import stats

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [7.03948302, 11.2347113, 15.3418565, 19.1049999, 23.2723955,
     27.4985445, 31.6573844, 35.81462, 39.5455326, 43.4423335]

slope, intercept, r, p, std_err = stats.linregress(x, y)


def compute(x):
    return slope * x + intercept


result = compute(4.5)
print(f"Nilai dari f(4.5) adalah {result}")
