import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def display_probability_distribution(probabilities):
    st.title('Probability Distribution')
    x = np.arange(len(probabilities))
    fig, ax = plt.subplots()
    ax.bar(x, probabilities)
    ax.set_xlabel('Categories')
    ax.set_ylabel('Probability')
    ax.set_xticks(x)
    ax.set_xticklabels(['Category {}'.format(i) for i in range(len(probabilities))])
    st.pyplot(fig)
