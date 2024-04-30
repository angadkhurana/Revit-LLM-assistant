
from dotenv import load_dotenv, find_dotenv
from langchain.document_loaders import TextLoader
from langchain.chains import ConversationalRetrievalChain
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.chains import VectorDBQA
from langchain.chains import RetrievalQA
load_dotenv(find_dotenv())
llm = ChatOpenAI()
# print(llm.predict("whats 5+5"))
import sys

q_string = "Tell me about" + sys.argv[1]
x = llm.predict(q_string)
print(x)




# def main():
#     # Check if there are command-line arguments
#     if len(sys.argv) > 1:
#         # Access the data passed as a command-line argument
#         received_data = sys.argv[1]
#         print(f"Received data in the other script: {received_data}")

#         # Use the received data (modify this part based on your use case)
#         processed_data = received_data.upper()
#         print(f"Processed data: {processed_data}")
#     else:
#         print("No data received in the other script.")

# main()
