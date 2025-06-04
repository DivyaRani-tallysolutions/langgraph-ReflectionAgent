import os
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("GOOGLE_API_KEY")


generation_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a professional LinkedIn writing assistant. Your goal is to write concise, engaging, and high-quality LinkedIn posts that match the user's request.\n\n"
        "- If the user provides only a prompt, write a post from scratch.\n"
        "- If the user shares critique, revise your previous response based on the feedback.\n"
        "- Always use a professional tone and aim for impact and clarity.\n"
        "- Limit the post to 3–6 short paragraphs or bullet points (under 300 words).\n"
        "- Avoid repetition. Start strong and end with a call to action or reflection."
    ),
    MessagesPlaceholder(variable_name="messages"),
])


reflection_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a viral LinkedIn assistant. Generate critique and recommendations for the user's post. "
        "Always provide detailed recommendations, including suggestions for length, virality, and style."
    ),
    MessagesPlaceholder(variable_name="messages"),
])


llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=OPENAI_API_KEY)

generation_chain = generation_prompt | llm
reflection_chain = reflection_prompt | llm
