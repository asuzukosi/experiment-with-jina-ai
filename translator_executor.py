from jina import Executor, requests
from docarray import DocumentArray, Document
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


class FrenchToEnglishTranslator(Executor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.tokenizer = AutoTokenizer.from_pretrained("facebook/mbart-large-50-many-to-many-mmt", src_lang="fr_XX")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
        
    @requests
    def translate(self, docs: DocumentArray, **kwargs):
        for doc in docs:
            doc.text = self._translate(doc.text)
            
    def _translate(self, text: Document):
        encoded_en = self.tokenizer(text, return_tensors="pt")
        generated_tokens = self.model.generate(**encoded_en, forced_bos_token_id=self.tokenizer.lang_code_to_id["en_XX"])
        return self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
        
        
            
    
