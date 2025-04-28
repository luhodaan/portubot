# state.py
import reflex as rx
import asyncio
from backend.portubot.portubot import PortugueseTutor

tutor = PortugueseTutor()

class State(rx.State):
    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    async def answer(self):
        # Our chatbot is not very smart right now...
        answer = await tutor.get_response(self.question)
        self.chat_history.append((self.question, answer))

        # Clear the question input.
        self.question = ""


