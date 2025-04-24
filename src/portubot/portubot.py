from dotenv import load_dotenv
import os
from pathlib import Path
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain_core.messages import HumanMessage
from langchain.chat_models import init_chat_model
# Optional: print the current working directory to make sure you're in the right place
print("Working directory:", os.getcwd())
#env_path = Path.cwd() / "src\\notebook\\.env"
#load_dotenv(dotenv_path=env_path)
# Load .env file from current directory or specify path if needed
#print(env_path)
load_dotenv()
# Test if it worked
print("LangSmith API Key:", os.getenv("LANGSMITH_PROJECT"))  # should print the value or None


model = init_chat_model("gpt-4o-mini", model_provider = "openai", temperature = 1)

prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are helping a user who is beginning to learn European Portuguese. "
            "They are fluent in Spanish, Italian, and English. "
            "Your goal is to help them expand their vocabulary, understand grammar better, and improve overall comprehension. "
            "To do this, propose short exercises that they can complete and return to you for corrections and feedback. "
            "Assume their current level is around A2, and gradually increase the difficulty as they improve. "
            "Each exercise should take between 5 to 10 minutes to complete. "
            "Always correct the user's mistakes, not just in their completed exercises but also in any message they send, including casual interactions. "
            "Use an informal tone and address the user using the second person (e.g., 'tu'). "
            "This is a command-line application, so **do not** use Markdown or any special formatting—output must be plain text only.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# Define a new graph
workflow = StateGraph(state_schema=MessagesState)


def call_model(state: MessagesState):
    prompt = prompt_template.invoke(state)
    response = model.invoke(prompt)
    return {"messages": response}


workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

memory = MemorySaver()
app = workflow.compile(checkpointer=memory)
configuration ={"configurable": {"thread_id": "1"}}

def stream_app_updates(user_input: str):
    for event in app.stream({"messages": [HumanMessage(content=user_input)]},config = configuration):
        print("João: ")
        for value in event.values():
            # If value is a BaseMessage (like AIMessage or HumanMessage), just print it
            print(value["messages"].content)

while True:
    try:
        user_input = input("Usuário: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        stream_app_updates(user_input)
    except KeyboardInterrupt:
        print("\nGoodbye!")
        break
    except Exception as e:
        print(f"Error: {e}")
        break