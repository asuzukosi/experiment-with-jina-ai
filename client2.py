from jina import Client, Document

client = Client(port=12345)  # use port from output above

french_text = Document(
    text='un astronaut est en train de faire une promenade dans un parc'
)

response = client.post(on='/', inputs=[french_text])

response[0].display()