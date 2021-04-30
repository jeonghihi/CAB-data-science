
# to know how "scaler" works 

#before sacling

sns.displot(
    wines, x="alcohol", col="wine_type",
    binwidth=3, height=8, facet_kws=dict(margin_titles=True),
)

sns.displot(
    wines, x="total sulfur dioxide", col="wine_type",
    binwidth=3, height=8, facet_kws=dict(margin_titles=True),
)


# apply scaler to array

from sklearn import preprocessing
import numpy as np
X_train = np.array([wines['total sulfur dioxide'], wines['alcohol'], wines['fixed acidity']])
scaler = preprocessing.StandardScaler().fit(X_train)
scaler
X_scaled = scaler.transform(X_train)
X_scaled

#after scaling

wines['total sulfur dioxide_scaled'] = X_scaled[0]
wines['alcohol_scaled'] = X_scaled[1]
wines['fixed acidity_scaled'] = X_scaled[2]

sns.displot(
    wines, x="alcohol_scaled", col="wine_type",
    binwidth=3, height=8, facet_kws=dict(margin_titles=True),
)

sns.displot(
    wines, x="total sulfur dioxide_scaled", col="wine_type",
    binwidth=3, height=8, facet_kws=dict(margin_titles=True),
)
