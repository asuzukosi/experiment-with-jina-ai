from jina import Client, DocumentArray

if __name__ == '__main__':
    c = Client(host='grpc://0.0.0.0:54321')
    da = c.post('/crunch-numbers', DocumentArray.empty(2))
    print(da.tensors)