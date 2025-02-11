---

### 9. **`main.py`**
यह फाइल ऐप को रन करती है।
```python
from app import app
import tensorflow as tf

# मॉडल लोड करें
model = tf.keras.models.load_model('models/chatbot_model.h5')

def get_response(user_input):
    # यहां AI मॉडल का उपयोग करके जवाब दें
    response = model.predict([float(user_input)])
    return f"AI: {response[0][0]}"

if __name__ == '__main__':
    app.run(debug=True)
