import random 
import streamlit as st

def guessing_game():
    low, high - 1, 100
    secret_number - random.randint(low, high)
    attempt = 0
    st.writer-(f"Welcome to the Number Guessing Game! I'm thinking of a number between {low} and {high}.")

    While True:
         try:
            guess - int(input{"Enter your guess:"})
            attempts +=1
         except ValueError:s
            st.wite("Please enter a valid integer.")
            continue

         if guess < secret_number:
            st.write("Too low! Try again.")
         elif guess > secret_number :
            st.write("Too high! Try again.")
         else:
            st.write(f"Congratulations! you've guessed the correct number {secret_number} in {attempts} attempts.")
            break

guessing_game()
