from pydantic import BaseModel
import gradio as gr

class InputModel(BaseModel):
    name: str
    id: int
    
class OutputModel(BaseModel):
    name: str
    othername: str
    

mappings = {
    str: gr.Textbox,
    int: gr.Number,
}

def get_gradio_interfaces(model):
    fields =  model.__fields__
    outputs = []
    for k,v in fields.items():
        intereface = mappings[v.type_]
        output = intereface(label=k)
        outputs.append(output)
    return outputs

print(get_gradio_interfaces(OutputModel))

def greet(*args, **kwargs):
    pass


def lauch_interfaces(inputModel, outputModel):
    demo = gr.Interface(
    fn=greet,
    inputs=get_gradio_interfaces(inputModel),
    outputs=get_gradio_interfaces(outputModel))
    demo.launch()

lauch_interfaces(inputModel=InputModel, outputModel=OutputModel)
