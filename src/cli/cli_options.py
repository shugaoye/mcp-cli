# src/cli/cli_options.py
import os
import json
from dotenv import load_dotenv

def process_options(server, disable_filesystem, provider, model):
    """
    Process CLI options to produce a list of server names and set environment variables.
    
    Returns a tuple of:
      - servers_list: The final list of server names.
      - user_specified: The list of servers specified by the user.
    """
    servers_list = []
    user_specified = []
    
    if server:
        # Allow comma-separated servers.
        user_specified = [s.strip() for s in server.split(",")]
        servers_list.extend(user_specified)
    
    # Always add 'filesystem' unless explicitly disabled.
    #if not disable_filesystem and "filesystem" not in servers_list:
    #    servers_list.insert(0, "filesystem")
        
    load_dotenv()
    # Use a default model if none is provided.
    default_provider = os.environ.get("LLM_PROVIDER", "openai")
    if default_provider:
        provider = default_provider

    if not model:
        model = os.environ.get("LLM_MODEL")
        if not model:
            if provider.lower() == "openai":
                model = "gpt-4o-mini"
            elif provider.lower() == "zhipuai":
                model = "glm-4-flash"
            elif provider.lower() == "ollama":
                "qwen2.5-coder"
    
    # Set environment variables used by the MCP code.
    os.environ["LLM_PROVIDER"] = provider
    os.environ["LLM_MODEL"] = model
    if not disable_filesystem:
        os.environ["SOURCE_FILESYSTEMS"] = json.dumps([os.getcwd()])
    
    return servers_list, user_specified
