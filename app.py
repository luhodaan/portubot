import dash
from dash import callback, html, Input, Output, State
from dash_chat import ChatComponent
from backend.portubot.portubot import PortugueseTutor

client = PortugueseTutor()

app = dash.Dash(__name__)

app.title = "Portubot"

app.layout = html.Div([
    ChatComponent(
        id="chat-component",
        input_placeholder="Escreve aqui...",
        messages=[],
        theme="light"
    )
])

@callback(
    Output("chat-component", "messages"),
    Input("chat-component", "new_message"),
    State("chat-component", "messages"),
    prevent_initial_call=True,
)
def handle_chat(new_message, messages):
    if not new_message:
        return messages

    updated_messages = messages + [new_message]

    if new_message["role"] == "user":
        print(new_message)
        response = client.get_response(new_message["content"])
        bot_response = {"role": "assistant", "content": response}
        return updated_messages + [bot_response]

    return updated_messages

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050, debug=True)