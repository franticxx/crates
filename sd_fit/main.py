import numpy as np
import polars as pl
import matplotlib.pyplot as plt
from iwo import IWO
from utils.stats import r2_score, var


def normal(miu, sigma, x, max_y):
    m1 = 1 / np.sqrt(2 * np.pi) * sigma
    m2 = np.exp(-((x - miu) ** 2) / 2 / sigma**2)
    y = m1 * m2
    y = y / y.max() * max_y
    return y


df = pl.read_csv("./fine600c_mono.csv").to_numpy().T
lam = df[0]
r = df[1]
idx = np.argmax(r)


def target_func(xn):
    if xn[0] <= 0:
        return 1e9
    y_pred = normal(miu=lam[idx], sigma=xn[0], x=lam, max_y=xn[1])
    v = var(r, y_pred)
    return v


iwo = IWO(
    func=target_func,
    min_x=0,
    max_x=10,
    gene_size=2,
)
xn, v = iwo.evlove()
print(xn)
print(v)
t = normal(lam[idx], xn[0], lam, xn[1])
print(r2_score(r, t))

plt.plot(lam, r)
plt.plot(lam, t)
plt.show()
