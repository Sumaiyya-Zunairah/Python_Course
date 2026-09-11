import streamlit as st
import random


def guess_number():

    st.header("Guess the Number!!!")

    if "secretNum" not in st.session_state:
        st.session_state.secretNum = random.randint(1, 10)

    guess = st.number_input(
        "Guess a number from 1 to 10", min_value=1,  max_value=10
    )

    if st.button("Guess"):

        if guess == st.session_state.secretNum:
            st.success("You got it!")

        elif guess < st.session_state.secretNum:
            st.write("Too low!")

        else:
            st.write("Too high!")


def rock_paper_scissors():

    st.header("Rock Paper Scissors")

    choice = st.selectbox(
        "Choose one:",
        ["Rock", "Paper", "Scissors"]
    )

    if st.button("Play"):

        computer = random.choice(
            ["Rock", "Paper", "Scissors"]
        )

        st.write("Computer chose:", computer)

        if choice == computer:
            st.write("Tie!")

        elif choice == "Rock" and computer == "Scissors":
            st.success("You win!")

        elif choice == "Paper" and computer == "Rock":
            st.success("You win!")

        elif choice == "Scissors" and computer == "Paper":
            st.success("You win!")

        else:
            st.error("You lose!")


st.title("Mini Games")

guess_number()
rock_paper_scissors()
