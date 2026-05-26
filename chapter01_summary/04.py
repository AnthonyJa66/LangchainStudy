# 导入和使用 WebBaseLoader
import dotenv
import os
from langchain_community.document_loaders import WebBaseLoader
import bs4

dotenv.load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("DEEPSEEK_API_KEY")
os.environ['OPENAI_BASE_URL'] = os.getenv("DEEPSEEK_BASE_URL")

loader = WebBaseLoader(
        web_path="https://www.gov.cn/zhengce/zhengceku/2020-12/04/content_5567010.htm",
        bs_kwargs=dict(parse_only=bs4.SoupStrainer(id="UCAP-CONTENT"))
    )
docs = loader.load()
# print(docs)

# 对于嵌入模型，这里通过 API调用
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")


from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 使用分割器分割文档
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
documents = text_splitter.split_documents(docs)
print(len(documents))
# 向量存储  embeddings 会将 documents 中的每个文本片段转换为向量，并将这些向量存储在 FAISS 向量数据库中
vector = FAISS.from_documents(documents, embeddings)