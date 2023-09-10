import pickle
import numpy as np

# Load the trained model
with open('diabetes_model.pkl', 'rb') as model_file:
    diabetes_model = pickle.load(model_file)

st.title('Diabetes Detection Test')

st.write("Note")

st.write(f"Please give input based on the changes what we did in the data")
# Get input features from the user
input_features = []

# Assuming you have a list of feature names
feature_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

for feature_name in feature_names:
    value = float(input(f"Enter value for {feature_name}: "))
    input_features.append(value)

# Convert input features to a NumPy array
input_features_array = np.array(input_features).reshape(1, -1)

# Make predictions using the loaded model
predicted_class = trained_model.predict(input_features_array)

print(f"Predicted class: {predicted_class[0]}")
