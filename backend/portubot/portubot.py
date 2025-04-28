from dotenv import load_dotenv
import os
from pathlib import Path
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain_core.messages import HumanMessage
from langchain.chat_models import init_chat_model


# print("Working directory:", os.getcwd())
load_dotenv()
# Test if it worked
print("LangSmith API Key:", os.getenv("LANGSMITH_PROJECT"))  # should print the value or None

class PortugueseTutor:
    def __init__(self):
        load_dotenv()
        self.model = init_chat_model("gpt-4o-mini",model_provider="openai",temperature=1)       
        self.memory = MemorySaver()
        self.workflow = self._build_workflow()
        self.configuration = {"configurable": {"thread_id": "1"}}
        self.prompt_template = self._create_prompt()

    def _build_workflow(self):
        workflow = StateGraph(state_schema = MessagesState)
        workflow.add_node("model", self.call_model)
        workflow.add_edge(START, "model")         
        return workflow.compile(checkpointer=self.memory)

    def call_model(self,state: MessagesState):
        prompt = self.prompt_template.invoke(state)
        response = self.model.invoke(prompt)
        return {"messages": response}
    
    def _create_prompt(self):
        return ChatPromptTemplate.from_messages(
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
    
    async def get_response(self, user_input: str):
        app = self.workflow
        events = app.stream(
            {"messages":
            [HumanMessage(content=user_input)]},
            config=self.configuration
        )

        full_response = []
        for event in events:
            for value in event.values():
                full_response.append(value["messages"].content)
            
        return "\n".join(full_response)






