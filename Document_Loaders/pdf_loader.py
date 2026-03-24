from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    '/Users/parleen/Desktop/langchain_models/Document_Loaders/2022_IEEE Transactions on Cybernetics.pdf'
)

docs= loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[0].metadata)