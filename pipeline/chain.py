from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationalRetrievalChain


def make_chain(vectorstore, model_name: str, k: int, memory, api_key: str):
    groq_llm = ChatGroq(api_key=api_key, model_name=model_name, temperature=0.5)

    prompt_template = """You are a helpful assistant. Answer the user using ONLY the provided context. If the answer is not in the context, say you don't know, do not guess.
Context: {context}
Chat history: {chat_history}
Question: {question}
Answer:
"""
    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "chat_history", "question"],
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": k})

    chain = ConversationalRetrievalChain.from_llm(
        llm=groq_llm,
        retriever=retriever,
        memory=memory,
        chain_type="stuff",
        combine_docs_chain_kwargs={"prompt": prompt},
        return_source_documents=True,
        output_key="answer",
        verbose=False,
    )
    return chain, retriever
