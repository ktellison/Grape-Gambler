
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

total_grapes = st.slider("Total number of grapes", 2, 1000, 10)
grapes_eaten = st.slider("Number of grapes you want to eat", 1, total_grapes, 1)
poison_grapes = st.slider("Number of poison grapes", 1, min(5, total_grapes - 1), 1)

if st.button("Eat the Grapes!"):
    survived, reward = simulate_grape_game(total_grapes, grapes_eaten, poison_grapes)
    if survived:
        st.success(f"You survived and earned ${reward:,}!")
    else:
        st.error("You ate the poison grape. You died!")

st.markdown("---")
st.subheader("Advanced: Run 1,000 simulations to see your survival rate")
if st.button("Run Simulations"):
    survival_count = 0
    for _ in range(1000):
        survived, _ = simulate_grape_game(total_grapes, grapes_eaten, poison_grapes)
        if survived:
            survival_count += 1
    st.info(f"Survival rate: {survival_count / 10:.1f}% over 1,000 trials.")
