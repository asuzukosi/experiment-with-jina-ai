from jina import Executor, requests, DocumentArray
import torch
import numpy as np

class MyExecutor(Executor):
    @requests
    def foo(self, docs: DocumentArray, **kwargs):
        docs[0].text = 'hello, world!'
        docs[1].text = 'goodbye, world!'
        
        
    @requests(on='/crunch-numbers')
    def bar(self, docs: DocumentArray, **kwargs):
        for doc in docs:
            doc.tensor = torch.tensor(np.random.random([10, 2]))
