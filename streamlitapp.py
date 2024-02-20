import streamlit as st
import pickle
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load model

with open('Models/model_tunned.pkl', 'rb') as f:
    model = pickle.load(f)


# Function to predict quality
def predict_quality(features):
    prediction = model.predict([features])
    return prediction[0]

# Streamlit app
def main():
    st.title('Apple Quality Predictor: Enhancing Your Fruit Selection Experience')

    st.write("""
    Our web application aims to revolutionize the way you select your apples by providing accurate predictions of their quality based on various key attributes. Whether you're a fruit enthusiast or someone looking for the perfect apple for your recipe, our tool is here to assist you.
    """)

    st.sidebar.header('Input Features')

    # Input features
    Size = st.sidebar.slider('Size', min_value=-7.15, max_value=6.14, step=0.01, value=0.0)
    Weight = st.sidebar.slider('Weight', min_value=-7.15, max_value=5.79, step=0.01, value=0.0)
    Sweetness = st.sidebar.slider('Sweetness', min_value=-6.89, max_value=6.37, step=0.01, value=0.0)
    Crunchiness = st.sidebar.slider('Crunchiness',  min_value=-6.06, max_value=7.62, step=0.01, value=0.0)
    Juiciness = st.sidebar.slider('Juiciness', min_value=-5.96, max_value=7.36, step=0.01, value=0.0)
    Ripeness = st.sidebar.slider('Ripeness', min_value=-5.86, max_value=7.24, step=0.01, value=0.0)
    Acidity = st.sidebar.slider('Acidity', min_value=-7.01, max_value=7.4, step=0.01, value=0.0)

    features = [Size, Weight, Sweetness, Crunchiness, Juiciness, Ripeness, Acidity]

    if st.sidebar.button('Predict'):
        quality = predict_quality(features)
        if quality == 0:
            st.success("The predicted quality of the apple is good.")
        elif quality == 1:
            st.error("The predicted quality of the apple is bad.")

    # Display input features as a table
    st.write("""
    ## Input Features
    Below are the input features provided by the user:
    """)
    input_df = pd.DataFrame({
        'Attribute': ['Size', 'Weight', 'Sweetness', 'Crunchiness', 'Juiciness', 'Ripeness', 'Acidity'],
        'Value': [Size, Weight, Sweetness, Crunchiness, Juiciness, Ripeness, Acidity]
    })
    st.table(input_df)

    # Display a radar chart of input features
    st.write("""
    ## Radar Chart of Input Features
    """)
    labels=np.array(['Size', 'Weight', 'Sweetness', 'Crunchiness', 'Juiciness', 'Ripeness', 'Acidity'])
    values=np.array([Size, Weight, Sweetness, Crunchiness, Juiciness, Ripeness, Acidity])

    angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
    values=np.concatenate((values,[values[0]]))
    angles=np.concatenate((angles,[angles[0]]))

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='blue', alpha=0.25)
    ax.plot(angles, values, color='blue', linewidth=2)

    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=12)

    st.pyplot(fig)

if __name__ == '__main__':
    main()