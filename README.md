# Portuguese Learning Assistant 🇵🇹🤖

A command-line chatbot designed to help users learn European Portuguese through interactive exercises and corrections. Built with LangChain and LangGraph.

## Features ✨

- **Personalized Learning**: Adapts to users fluent in Spanish, Italian, and English
- **Interactive Exercises**: 5-10 minute vocabulary and grammar exercises
- **Real-time Corrections**: Fixes mistakes in both exercises and casual conversation
- **Progress Tracking**: Maintains conversation memory with LangGraph
- **CLI Interface**: Simple text-based interaction

## Prerequisites 🛠️

- Python 3.13+
- [Poetry](https://python-poetry.org/) (recommended) or pip
- OpenAI API key (or other supported LLM provider)
- LangSmith API key (optional for tracing)

## Installation 📥

1. **Clone the repository**:
   ```sh
   git clone https://github.com/luhodaan/portubot.git
   cd portubot

## Quick Start 🚀

1. **Build the image:**
```sh
docker compose build
```

2. **Launch the CLI app:**
```sh
docker compose run --rm app
```