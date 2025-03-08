# Model Context Provider CLI
This repository contains a protocol-level CLI designed to interact with a Model Context Provider server. The client allows users to send commands, query data, and interact with various resources provided by the server.

## Features
- Protocol-level communication with the Model Context Provider.
- Dynamic tool and resource exploration.
- Support for multiple providers and models:
  - Providers: OpenAI, Ollama.
  - Default models: `gpt-4o-mini` for OpenAI, `qwen2.5-coder` for Ollama.
- Enhanced modular chat system with server-aware tools.
- Rich command system with context-aware completions.

## Prerequisites
- Python 3.8 or higher.
- Required dependencies (see [Installation](#installation))
- If using ollama you should have ollama installed and running.
- If using openai you should have an api key set in your environment variables (OPENAI_API_KEY=yourkey)

## Installation
1. Clone the repository:

```bash
git clone https://github.com/chrishayuk/mcp-cli
cd mcp-cli
```

2. Install UV:

```bash
pip install uv
```

3. Resynchronize dependencies:

```bash
uv sync --reinstall
```

## Usage
To start the client and interact with the SQLite server, run the following command:

```bash
uv run mcp-cli --server sqlite
```

### Command-line Arguments
- `--server`: Specifies the server configuration to use. Required.
- `--config-file`: (Optional) Path to the JSON configuration file. Defaults to `server_config.json`.
- `--provider`: (Optional) Specifies the provider to use (`openai` or `ollama`). Defaults to `openai`.
- `--model`: (Optional) Specifies the model to use. Defaults depend on the provider:
  - `gpt-4o-mini` for OpenAI.
  - `llama3.2` for Ollama.

### Examples
Run the client with the default OpenAI provider and model:

```bash
uv run mcp-cli --server sqlite
```

Run the client with a specific configuration and Ollama provider:

```bash
uv run mcp-cli --server sqlite --provider ollama --model llama3.2
```

## Interactive Mode
The client supports interactive mode, allowing you to execute commands dynamically. Type `help` for a list of available commands or `quit` to exit the program.

## Supported Commands
- `ping`: Check if the server is responsive.
- `list-tools`: Display available tools.
- `list-resources`: Display available resources.
- `list-prompts`: Display available prompts.
- `chat`: Enter interactive chat mode.
- `clear`: Clear the terminal screen.
- `help`: Show a list of supported commands.
- `quit`/`exit`: Exit the client.

### Chat Mode
To enter chat mode and interact with the server:

```bash
uv run mcp-cli main.py --server sqlite
```

In chat mode, you can use tools and query the server interactively. The provider and model used are specified during startup and displayed in the welcome banner.

#### Chat Commands
While in chat mode, you can use the following slash commands:

- `/tools`: Display all available tools with their server information
  - `/tools --all`: Show detailed tool information including parameters
  - `/tools --raw`: Show raw tool definitions
- `/cls`: Clear the screen while keeping conversation history
- `/clear`: Clear both the screen and conversation history
- `/compact`: Condense conversation history into a summary
- `/save <filename>`: Save conversation history to a JSON file
- `/help`: Show available commands
- `/help <command>`: Show detailed help for a specific command

Type `exit` or `quit` to leave chat mode.

#### Using OpenAI Provider:
If you wish to use openai models, you should:

- Set the `OPENAI_API_KEY` environment variable before running the client, either in .env or as an environment variable.

## Project Structure

The project follows a modular architecture:

```
src/
├── cli/
│   ├── chat/
│   │   ├── commands/         # Chat slash commands
│   │   ├── chat_context.py   # Chat state management
│   │   ├── chat_handler.py   # Main chat logic
│   │   ├── conversation.py   # Conversation processing
│   │   ├── ui_helpers.py     # UI utilities
│   │   └── ui_manager.py     # User interface management
│   ├── commands/             # Main CLI commands
│   └── ...
├── llm/                      # LLM client and tools
└── ...
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request with your proposed changes.

## License
This project is licensed under the [MIT License](license.md).