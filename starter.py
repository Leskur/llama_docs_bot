from llama_index import download_loader

RemoteReader = download_loader("RemoteReader")
loader = RemoteReader()
documents = loader.load_data(url="https://www.gov.cn/zhuanti/2015qgwebpc/wenti.pdf")

for document in documents:
    print(document, end="\n\n")
