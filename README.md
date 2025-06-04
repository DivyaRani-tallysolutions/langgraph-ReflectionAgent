# LangGraph Reflection Agent

A smart LinkedIn writing assistant built with [LangGraph](https://github.com/langchain-ai/langgraph) and Google's Gemini (`gemini-1.5-flash`). 
This tool uses a **generator agent** to craft LinkedIn posts and a **reflector agent** to critique and suggest improvements.

## Features

- **Post Generation**: Creates concise, high-impact LinkedIn posts based on user prompts.
- **Reflection Agent**: Evaluates posts with detailed critique on clarity, length, tone, and virality.
- **Iterative Improvement**: Posts are regenerated until critiques become short and satisfied.
- Built using `LangChain`, `LangGraph`, and `Gemini`.
