# src/llm/providers/openai_client.py
import os
import logging
from typing import Any, Dict, List
from dotenv import load_dotenv

# zhipuai
from zhipuai import ZhipuAI

# llm imports
from llm.providers.base import BaseLLMClient

# Load environment variables
load_dotenv()

class ZhipuAILLMClient(BaseLLMClient):
    def __init__(self, model="glm-4-flash", api_key=None):
        # set the model
        self.model = model

        # set the api key
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")

        # check for an api key
        if not self.api_key:
            raise ValueError("The OPENAI_API_KEY environment variable is not set.")
        
        # set the client as open ai
        self.client = ZhipuAI(api_key=self.api_key)

    def create_completion(self, messages: List[Dict], tools: List = None) -> Dict[str, Any]:
        try:
            # perform the completion
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=tools or [],
            )

            # return the response
            return {
                "response": response.choices[0].message.content,
                "tool_calls": getattr(response.choices[0].message, "tool_calls", []),
            }
        except Exception as e:
            # error
            logging.error(f"ZhipuAI API Error: {str(e)}")
            raise ValueError(f"ZhipuAI API Error: {str(e)}")
