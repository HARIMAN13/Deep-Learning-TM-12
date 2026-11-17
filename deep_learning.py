import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.metrics import confusion_matrix, classification_report

df = pd.read_excel('BlaBla.xlsx')

df['UMUR_TAHUN'] = pd.to_numeric(df['UMUR_TAHUN'], errors='coerce')
print(df.isnull().sum())
df = df.dropna().reset_index(drop=True)

def encode_umur(val):
    if val <= 20:
        return 1
    elif val <= 30:
        return 2
    elif val <= 40:
        return 3
    elif val <= 50:
        return 4
    else:
        return 5

df['Umur'] = df['UMUR_TAHUN'].apply(encode_umur)

q1 = df['UMUR_TAHUN'].quantile(0.25)
q3 = df['UMUR_TAHUN'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = df[(df['UMUR_TAHUN'] < lower_bound) | (df['UMUR_TAHUN'] > upper_bound)]
print(len(outliers))

X = df[['Umur', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']]
y = df['N']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = Sequential([
    Dense(16, activation='relu', input_shape=(X.shape[1],)),
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=100, validation_split=0.2, verbose=1)

loss, acc = model.evaluate(X_test, y_test, verbose=0)
print(f'\nAkurasi di data uji: {acc * 100:.2f}%')

y_pred = (model.predict(X_test) > 0.5).astype(int)
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=[0, 1], yticklabels=[0, 1])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.savefig('confusion_matrix.png')
plt.close()

print('\nClassification Report:')
print(classification_report(y_test, y_pred))
