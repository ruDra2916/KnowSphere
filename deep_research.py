import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager

load_dotenv(override=True)


async def run(query: str):
    async for chunk in ResearchManager().run(query):
        yield chunk


with gr.Blocks(
    theme=gr.themes.Default(primary_hue="pink"),
    css="""
        #title {
            font-size: 2.5rem;
            text-align: center;
            font-weight: bold;
            color: #fffdd0; /* Creamy white */
            margin-bottom: 0.5rem;
        }
        #subtitle {
            text-align: center;
            font-size: 1.1rem;
            color: #bbb;
            margin-bottom: 1.5rem;
        }
        #output-box {
            background-color: #2a2a3a;
            padding: 1.5rem;
            border-radius: 16px;
            color: #f3f3f3;
            font-size: 1rem;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
            min-height: 300px;
        }
    """
) as ui:
    with gr.Column():
        gr.Markdown("<div id='title'>🧠 KnowSphere</div>")
        gr.Markdown("<div id='subtitle'>Explore research topics with style and intelligence</div>")

    with gr.Row():
        with gr.Column(scale=1, min_width=350):
            gr.Markdown("### 🔍 What topic would you like to explore?")
            query_textbox = gr.Textbox(
                label="Research Topic",
                placeholder="e.g., Ethical Concerns in AI",
                lines=1,
                max_lines=1,
                autofocus=True
            )
            run_button = gr.Button("✨ Generate Report", variant="primary", size="lg")
            gr.Markdown("➡️ Research summary appears on the right")

        with gr.Column(scale=2, min_width=500):
            gr.Markdown("### 📑 Report Summary")
            report = gr.Markdown(
                "Please enter a topic and click **Generate Report** to begin.",
                elem_id="output-box"
            )

    run_button.click(fn=run, inputs=query_textbox, outputs=report)
    query_textbox.submit(fn=run, inputs=query_textbox, outputs=report)

ui.launch(inbrowser=True)