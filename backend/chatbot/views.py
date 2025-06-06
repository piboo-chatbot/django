from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from langchain_openai import ChatOpenAI
from chatbot.chain import get_chain
from retriever.utils import (
    set_embedding_model, load_chromadbs, create_ensemble_retriever, search_documents
)

from chatbot.qlora import load_qlora_llm

# (초기화 작업: 임베딩/리트리버/체인 등)
embedding_model = set_embedding_model()
chroma1, chroma2 = load_chromadbs(embedding_model)
ensemble_retriever = create_ensemble_retriever(chroma1, chroma2)
llm_model = ChatOpenAI(model_name='gpt-4o-mini', temperature=0.4)
# qlora_model= load_qlora_llm(
#         base_model_path="beomi/KoAlpaca-Polyglot-5.8B",
#         adapter_path="./qlora_model_koalpaca"
#     )
# chat_memory = get_chain(qlora_model)#llm_model
chat_memory = get_chain(llm_model)

def chatbot_page(request):
    return render(request, 'chatbot.html')

class AskView(APIView):
    def post(self, request):
        query = request.data.get('query')
        session_id = request.data.get('session_id')
        search_results = search_documents(ensemble_retriever, query)
        response = chat_memory.invoke(
            {"query": query, "search_results": search_results},
            config={"configurable": {"session_id": session_id}}
        )
        return Response({"answer": response.content}, status=status.HTTP_200_OK)