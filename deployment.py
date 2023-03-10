from translator_executor import FrenchToEnglishTranslator
from jina import Deployment

with Deployment(uses=FrenchToEnglishTranslator, timeout_ready=-1) as dep:
    dep.block()