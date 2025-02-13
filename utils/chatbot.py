import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set API Key securely from environment
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Initialize Groq's LLaMA model
llama = ChatGroq(model_name="llama3-8b-8192")  # Use "llama3-70b" for a larger model

def get_chatbot_response(user_input):
    try:
        # Construct a simple string prompt
        prompt = f"You are a helpful AI assistant. Respond to the following question: {user_input}"

        # Get chatbot's response based on the user input
        response = llama.invoke(prompt)

        # Check if the response contains valid content
        if not response.content:
            return "Sorry, I couldn't generate a response. Please try again."

        # Return the chatbot's response content
        return response.content
    except Exception as e:
        return f"Error generating response: {str(e)}"
