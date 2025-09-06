import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Iris Species Prediction 🌸",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #FF6B6B;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .prediction-box {
        background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
        color: white;
        padding: 2rem;
        border-radius: 1rem;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
    }
    .stButton > button {
        background: linear-gradient(135deg, #FF6B6B 0%, #ee5a52 100%);
        color: white;
        border: none;
        border-radius: 0.5rem;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s ease;
        width: 100%;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .info-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def get_model_info():
    """Get information about Random Forest model"""
    models = {
        'Random Forest': {
            'description': 'Ensemble of decision trees with random sampling and bootstrap aggregating',
            'best_for': 'High accuracy, robust predictions, feature importance analysis',
            'pros': ['Reduces overfitting', 'Handles missing values', 'Feature importance', 'Robust to outliers', 'Works well with mixed data types'],
            'cons': ['Less interpretable than single trees', 'Can be slow for very large datasets', 'Memory intensive']
        }
    }
    return models

def main():
    # Header
    st.markdown('<h1 class="main-header">🌸 Iris Species Prediction</h1>', unsafe_allow_html=True)
    
    # Add large image if available
    try:
        # Try different possible image paths
        image_paths = [
            'iris-machinelearning.png',
            '../iris-machinelearning.png',
            'Data/iris-machinelearning.png',
            '../Data/iris-machinelearning.png'
        ]
        
        image_found = False
        for img_path in image_paths:
            try:
                # Create a centered container for the large image
                col1, col2, col3 = st.columns([1, 3, 1])
                with col2:
                    st.image(img_path, width=900, caption="Iris Flower - Sepal & Petal Parts")
                image_found = True
                break
            except:
                continue
        
        if not image_found:
            # If no image found, show a large placeholder
            st.markdown("""
            <div style="text-align: center; margin: 40px 0;">
                <div style="font-size: 10rem; color: #FF6B6B; margin-bottom: 20px;">🌸</div>
                <h2 style="color: #666; font-style: italic; margin-bottom: 10px;">Iris Flower Classification</h2>
                <p style="color: #888; font-size: 1.2rem;">Add an iris flower image to enhance the visual experience</p>
            </div>
            """, unsafe_allow_html=True)
    except:
        pass
    
    # Get model information
    models = get_model_info()
    
    # Info box
    st.markdown("""
    <div class="info-box">
        <h4>🎯 Iris Species Prediction</h4>
        <p>Enter the measurements of an iris flower to predict its species using machine learning models.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Input form
    st.markdown("## 📏 Enter Flower Measurements")
    
    col1, col2 = st.columns(2)
    
    with col1:
        sepal_length = st.slider("Sepal Length (cm)", 
                                min_value=0.0, max_value=10.0, 
                                value=5.8, step=0.1)
        sepal_width = st.slider("Sepal Width (cm)", 
                               min_value=0.0, max_value=10.0, 
                               value=3.0, step=0.1)
    
    with col2:
        petal_length = st.slider("Petal Length (cm)", 
                                min_value=0.0, max_value=10.0, 
                                value=4.3, step=0.1)
        petal_width = st.slider("Petal Width (cm)", 
                               min_value=0.0, max_value=10.0, 
                               value=1.3, step=0.1)
    
    # Model information
    st.markdown("## 🤖 Random Forest Model")
    selected_model = "Random Forest"
    
    # Show model info
    with st.expander("ℹ️ About Random Forest Algorithm"):
        model_info = models[selected_model]
        st.write(f"**Description:** {model_info['description']}")
        st.write(f"**Best for:** {model_info['best_for']}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Advantages:**")
            for pro in model_info['pros']:
                st.write(f"✅ {pro}")
        with col2:
            st.write("**Limitations:**")
            for con in model_info['cons']:
                st.write(f"❌ {con}")
        
        st.markdown("""
        **How Random Forest Works:**
        1. Creates multiple decision trees using bootstrap sampling
        2. Each tree uses a random subset of features
        3. Final prediction is the majority vote of all trees
        4. This ensemble approach reduces overfitting and improves accuracy
        """)
    
    # Prediction button
    if st.button("🔮 Predict Species", type="primary"):
        # Simulate prediction based on input values (demo mode)
        species_mapping = {0: 'Iris-setosa', 1: 'Iris-versicolor', 2: 'Iris-virginica'}
        
        # Simple rule-based prediction for demo
        if petal_length < 2.5:
            prediction = 0  # Iris-setosa
        elif petal_length < 5.0:
            prediction = 1  # Iris-versicolor
        else:
            prediction = 2  # Iris-virginica
        
        predicted_species = species_mapping[prediction]
        
        # Simulate probabilities
        probabilities = [0.1, 0.1, 0.1]
        probabilities[prediction] = 0.8
        
        # Display results
        st.markdown("## 🎯 Prediction Results (Demo Mode)")
        
        st.info("⚠️ **Demo Mode**: This is a simplified prediction for demonstration purposes. In a real application, trained ML models would be used.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div class="prediction-box">
                <h3>Predicted Species: {predicted_species}</h3>
                <p>Model: {selected_model} (Demo)</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("**Prediction Probabilities:**")
            for i, prob in enumerate(probabilities):
                species_name = species_mapping[i]
                st.write(f"{species_name}: {prob:.3f}")
        
        # Show input values
        st.markdown("### 📊 Input Values Used")
        input_df = pd.DataFrame({
            'Feature': ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'],
            'Value (cm)': [sepal_length, sepal_width, petal_length, petal_width]
        })
        st.dataframe(input_df, use_container_width=True)
        
        # Species information
        st.markdown("### 🌸 About the Predicted Species")
        if predicted_species == 'Iris-setosa':
            st.info("**Iris-setosa**: Smallest species with short, wide petals. Typically found in cool climates.")
        elif predicted_species == 'Iris-versicolor':
            st.info("**Iris-versicolor**: Medium-sized species with moderate petal dimensions. Common in temperate regions.")
        elif predicted_species == 'Iris-virginica':
            st.info("**Iris-virginica**: Largest species with long, narrow petals. Found in warmer climates.")
    
    # Footer
    st.markdown("---")
    st.markdown("**Built with ❤️ using Streamlit**")

if __name__ == "__main__":
    main()
