from jina import DocumentArray, Executor, requests


class TestExecutor(Executor):
    """"""
    @requests
    def foo(self, docs: DocumentArray, **kwargs):
        pass