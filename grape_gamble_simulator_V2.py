import streamlit as st
import random

def simulate_grape_game(total_grapes, grapes_eaten, poison_grapes=1):
    grapes = ['poison'] * poison_grapes + ['safe'] * (total_grapes - poison_grapes)
    random.shuffle(grapes)
    chosen_grapes = random.sample(grapes, grapes_eaten)
    if 'poison' in chosen_grapes:
        return False, 0
    else:
        return True, grapes_eaten * 100_000

st.title("Grape Gamble Simulator")
st.markdown("Simulate your odds in a deadly game of chance. One grape is poison. The others are worth $100,000 each.")

st.subheader
