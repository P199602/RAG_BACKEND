from app.rag import search_pdf
from app.ai import get_ai_response


def chatbot_response(question):

    # Search PDF context
    context = search_pdf(question)

    # If context found in PDF
    if context and len(context.strip()) > 20:

        prompt = f"""
        You are an AI PDF Assistant.

        Answer from the PDF context below.

        PDF Context:
        {context}

        User Question:
        {question}

        Rules:
        - Reply in same language as user
        - Hindi supported
        - Hinglish supported
        - Explain clearly
        """

    else:

        # Normal AI Chat
        prompt = f"""
        You are a smart AI assistant.

        User Question:
        {question}

        Rules:
        - Reply naturally
        - Hindi supported
        - Hinglish supported
        - Friendly communication
        """

    response = get_ai_response(prompt)

    return response 