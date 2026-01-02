from langchain_astradb import AstraDBVectorStore
#from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

from .data_converter import DataConverter
from .config import Config

class DataIngestor:
    def __init__(self):
        self.embedding = HuggingFaceEmbeddings(model_name=Config.EMBEDDING_MODEL)

        self.vstore = AstraDBVectorStore(
            embedding=self.embedding,
            collection_name="vehicle_data_v2",
            api_endpoint=Config.ASTRA_DB_API_ENDPOINT,
            token=Config.ASTRA_DB_APPLICATION_TOKEN,
            namespace=Config.ASTRA_DB_KEYSPACE
        )

    def ingest(self,load_existing=True):
        if load_existing==True:
            return self.vstore
        
        docs = DataConverter("data/v2-carapi-datafeed-sample.xlsx").convert()

        self.vstore.add_documents(docs)

        return self.vstore

