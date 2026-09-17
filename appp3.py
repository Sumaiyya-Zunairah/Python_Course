import streamlit as st
from ollama import chat


# -----------------------------
# PAGE DESIGN
# -----------------------------

st.markdown("""
<style>

    /* Overall background */
    .stApp {
        background-color: #EAF4E3;
    }

    /* ALL TEXT */
    html, body, [class*="css"],
    p, span, div, label, button, input, textarea {
        font-family: "Times New Roman", Times, serif !important;
        color: #0B3018 !important;
    }

    /* Main title */
    h1 {
        color: #0B3018 !important;
        text-align: center;
        font-family: "Times New Roman", Times, serif !important;
    }

    /* Header */
    h2 {
        color: #0B3018 !important;
        text-align: center;
        font-family: "Times New Roman", Times, serif !important;
    }

    /* Normal text */
    p {
        color: #0B3018 !important;
        font-family: "Times New Roman", Times, serif !important;
    }

    /* Text area */
    textarea {
        background-color: #F7FBF4 !important;
        color: #0B3018 !important;
        border: 2px solid #285C35 !important;
        border-radius: 12px !important;
        font-family: "Times New Roman", Times, serif !important;
    }

    /* Text area placeholder */
    textarea::placeholder {
        color: #315B3D !important;
        opacity: 1 !important;
        font-family: "Times New Roman", Times, serif !important;
    }

    /* Text area label */
    label {
        color: #0B3018 !important;
        font-family: "Times New Roman", Times, serif !important;
    }

    /* Send button */
    .stButton > button {
        background-color: #285C35 !important;
        color: #EAF4E3 !important;
        border: 2px solid #0B3018 !important;
        border-radius: 12px !important;
        padding: 10px 25px;
        font-family: "Times New Roman", Times, serif !important;
        font-size: 16px;
        font-weight: bold;
    }

    /* Send button hover */
    .stButton > button:hover {
        background-color: #183F24 !important;
        color: #EAF4E3 !important;
    }

    /* Chat messages */
    .message-text {
        font-family: "Comic Sans MS", "Comic Sans", cursive !important;
        color: #0B3018 !important;
        font-size: 18px;
    }

    /* Make message text stay Comic Sans */
    .message-text * {
        font-family: "Comic Sans MS", "Comic Sans", cursive !important;
        color: #0B3018 !important;
    }

    /* Expander */
    [data-testid="stExpander"] {
        color: #0B3018 !important;
        border-color: #285C35 !important;
    }

    [data-testid="stExpander"] * {
        color: #0B3018 !important;
        font-family: "Times New Roman", Times, serif !important;
    }

</style>
""", unsafe_allow_html=True)


# -----------------------------
# OLLAMA MODEL
# -----------------------------

model_name = "llama3.2"


def get_response(model, message):

    response = chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
    )

    return response.message.content


# -----------------------------
# APP TITLE
# -----------------------------

st.title(" ──.🍀 ݁˖༘⋆─Green─.🍀 ݁˖༘⋆──")

st.header("✩°𓏲⋆🪲Welcome to our AI Chatbox🪲✩°𓏲⋆")


# -----------------------------
# CHAT FORM
# -----------------------------

with st.form("⋆𓂃 𓈒𓏸🪷˚｡⋆message⋆✴︎˚𓂃 𓈒𓏸🪷⋆"):

    message = st.text_area(
        "⋆✴︎˚｡⋆Type your message! ₊✩‧₊˚౨ৎ˚₊✩‧₊ :"
    )

    submit_button = st.form_submit_button("Send!⋆˚࿔")


# -----------------------------
# RESPONSE
# -----------------------------

if submit_button:

    if message:

        response = get_response(model_name, message)

        # User message
        st.markdown(
            f"""
            <p class="message-text">
                <b>You:</b> {message}
            </p>
            """,
            unsafe_allow_html=True
        )

        # Ollama response
        st.markdown(
            f"""
            <p class="message-text">
                <b>OLLAMA:</b> {response}
            </p>
            """,
            unsafe_allow_html=True
        )

    else:

        st.error("Please type a message ˚˖𓍢ִ໋`🌿: ")