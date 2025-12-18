import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib


# Data contoh
# luas_bangunan (m2) dan harga_rumah (juta rupiah)
data = {
'luas_bangunan': [36, 45, 60, 72, 90, 120],
'harga_rumah': [150, 200, 300, 380, 500, 650]
}


df = pd.DataFrame(data)


# Fitur dan target
X = df[['luas_bangunan']]
y = df['harga_rumah']


# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Training model
model = LinearRegression()
model.fit(X_train, y_train)


# Simpan model
joblib.dump(model, 'house_price_model.pkl')
