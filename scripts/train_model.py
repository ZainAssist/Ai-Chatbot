import numpy as np
import tensorflow as tf

# डेटा तैयार करें
X = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 6, 8, 10], dtype=float)

# सरल मॉडल बनाएं
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

# मॉडल को कंपाइल करें
model.compile(optimizer='sgd', loss='mean_squared_error')

# मॉडल को ट्रेन करें
model.fit(X, y, epochs=500)

# मॉडल को सेव करें
model.save('models/chatbot_model.h5')
