from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.vectorstores.faiss import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain


class ChatPDF:
    def __init__(self) -> None:
        pass

    def get_pdf_text(self, pdf_docs):
        text = ""
        for pdf in pdf_docs:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                text += page.extract_text()
        return text

    def get_text_chunks(self, text):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=5000, chunk_overlap=2000
        )
        chunks = text_splitter.split_text(text=text)
        return chunks

    def get_vector_stores(self, chunks):
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vector_store = FAISS.from_texts(texts=chunks, embedding=embeddings)
        vector_store.save_local("faiss_index")

    def get_conversation_chain(self):
        prompt_template = """
        Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in provided context just say, 
        "Answer is not available in the given context.", don't provide the wrong answer\n\n
        Context:\n {context}?\n
        Question: \n{question}\n

        Answer:
        """
        model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.4)
        prompt = PromptTemplate(
            input_variables=["context", "question"], template=prompt_template
        )
        chain = load_qa_chain(llm=model, prompt=prompt, chain_type="stuff")
        return chain

    def get_user_input(self, question):
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        database = FAISS.load_local("faiss_index", embeddings)
        docs = database.similarity_search(question)
        chain = self.get_conversation_chain()

        response = chain(
            {"input_documents": docs, "question": question}, return_only_outputs=True
        )
        return response
