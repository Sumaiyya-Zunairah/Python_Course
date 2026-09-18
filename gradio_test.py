import gradio as gr
from ollama import chat

model_name = "llama3.2"


def chatbot(message, history):
    response = chat(
        model=model_name,
        messages=[
            {"role": "user", "content": message}
        ]
    )

    return response["message"]["content"]


with gr.Blocks(
    title="🌊 Aqua AI",
    theme=gr.themes.Soft(
        primary_hue="blue",
        secondary_hue="cyan",
        neutral_hue="slate"
    )
) as demo:

    gr.Markdown(
        """
        # 🌊 Aqua AI
        ### 🐚 Your ocean-themed AI companion
        """
    )

    gr.Markdown(
        """
        🌊 Welcome to Aqua AI!

        Ask me anything and I'll do my best to help.
        
        🐠 🐚 🫧 🪼
        """
    )

    gr.Markdown("see anything fishy latley?")

    chatbot_ui = gr.Chatbot(
        height=300
    )

    with gr.Row():
        message_box = gr.Textbox(
            placeholder="Ask Aqua AI something... 🌊",
            label="Your message",
            scale=4
        )

        send_button = gr.Button(
            "🌊 Send",
            scale=4
        )

    def send_message(message, history):

        response = chatbot(message, history)

        history.append(
            {"role": "user", "content": message}
        )

        history.append(
            {"role": "assistant", "content": response}
        )

        return "", history

    send_button.click(
        send_message,
        inputs=[message_box, chatbot_ui],
        outputs=[message_box, chatbot_ui]
    )


demo.launch()