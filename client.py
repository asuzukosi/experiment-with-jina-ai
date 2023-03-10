from docarray import Document
from jina import Client

french_text = Document(
    text='un astronaut est en train de faire une promenade dans un parc'
)

client = Client(port=51106)  # use port from output above
response = client.post(on='/', inputs=[french_text])

print(response[0].text)