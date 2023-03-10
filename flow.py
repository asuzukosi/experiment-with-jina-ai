from jina import Flow
from translator_executor import FrenchToEnglishTranslator

flow = Flow().add(uses=FrenchToEnglishTranslator, timeout_ready=-1).add(uses='jinaai://jina-ai/TextToImage',timeout_ready=-1,install_requirements=True)

with flow:
    flow.block()