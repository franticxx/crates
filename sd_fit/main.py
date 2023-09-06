import numpy as np
import polars as pl
import matplotlib.pyplot as plt
from iwo import IWO
from scipy import interpolate
from utils.stats import r2_score, var
from utils.linalg import skew


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
    # y_pred = normal(miu=lam[idx], sigma=xn[0], x=lam, max_y=xn[1])
    y_pred = skew(x=lam, y=r, s1=xn[2], s2=[3], idx=idx)
    y_pred = y_pred / y_pred.max() * r.max()
    # f = interpolate.interp1d(lam, r)
    # y_pred = f(lam_)
    v = var(r, y_pred)
    return v


iwo = IWO(func=target_func, min_x=0, max_x=2, gene_size=4, gmax=10, is_show=True)
xn, v = iwo.evlove()
print(xn)
print(v)
# t = normal(lam[idx], xn[0], lam, xn[1])
t = skew(x=lam, y=r, s1=xn[2], s2=[3], idx=idx)
t = t / t.max() * r.max()
print(r2_score(r, t))

plt.plot(lam, r)
plt.plot(lam, t)
plt.show()
