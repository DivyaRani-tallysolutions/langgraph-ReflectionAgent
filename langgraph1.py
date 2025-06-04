from langchain_core.messages import HumanMessage
from langgraph.graph import END, MessageGraph

from chain import generation_chain, reflection_chain

REFLECT = "reflect"
GENERATE = "generate"

graph = MessageGraph()


def generate_node(state):
    print("\nGenerate Node Called")

    response = generation_chain.invoke({"messages": state})

    return response


def reflect_node(messages):
    print("\nReflect Node Called")

    response = reflection_chain.invoke({"messages": messages})

    return response.content  # returning string content


def should_continue(state):
    if len(state) > 6:
        return END
    else:

        return REFLECT


graph.set_entry_point(GENERATE)
graph.add_node(GENERATE, generate_node)
graph.add_node(REFLECT, reflect_node)
graph.add_edge(REFLECT, GENERATE)
graph.add_conditional_edges(GENERATE, should_continue)

app = graph.compile()


def print_conversation(messages):
    for i, msg in enumerate(messages, 1):
        sender = "User" if msg.__class__.__name__ == "HumanMessage" else "AI"

        print(
            f"\n------------------------------------- Message {i} ({sender}) -------------------------------------------------------------------------------------------"
        )
        print(
            "---------------------------------------------------------------------------------------------------------------------------------------------------------"
        )
        print(msg.content.strip())
    print("\n=== End of Conversation ===\n")


print("=== Starting LangGraph Pipeline ===")
response = app.invoke(
    HumanMessage(
        content="Write a LinkedIn post about getting a new job as a intern at Tally Solutions. Keep it humble but enthusiastic."
    )
)

print_conversation(response)
