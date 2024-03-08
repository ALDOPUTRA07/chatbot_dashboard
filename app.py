import gradio as gr

from model.model import model

# Making question examples
example1 = "Apa dashboard terkait KPI operational?"
example2 = "Apa link Dashboard Operational KPIs 2023?"
example3 = "Mau lihat data performance cabang, ada di dashboard apa?"
example4 = "Apa saja data di Dashboard Transactions?"

# Making UI
with gr.Blocks() as demo:
  gr.Markdown(
  """
  # Chatbot Dashboard
  This project is a chatbot based on LLM using the RAG method. 
  This chatbot will answer questions related to the company's dashboard. 
  You can ask questions according to the dashboard data below.
  """)
  gr.Interface(fn=model,
             inputs="text",
             outputs="text",
             theme=gr.themes.Monochrome(),
             examples = [example1, example2, example3, example4])
  gr.Markdown(
    """
    ## Data dashboard
    """)
  gr.HTML("<img src='https://huggingface.co/spaces/Aldo07/new1233/resolve/main/data%20dashboard.png' width='500'>")

demo.launch()

