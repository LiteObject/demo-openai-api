import gradio as gr

def greet(name, intensity):
    return "Hello " * intensity + name + "!"

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

# demo.launch(share=True)  # Share your demo with just 1 extra parameter 🚀
demo.launch()
