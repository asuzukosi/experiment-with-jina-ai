from typing import Dict, Any

import bentoml
import pandas as pd
from bentoml.io import JSON

model_runner = bentoml.models.get('default.amount_prediction:ugrehggbf6jswgqc').to_runner()
svc = bentoml.Service("default.amount_prediction", runners=[model_runner])


@svc.api(input=JSON(), output=JSON())
def predict(input_data: Dict[str, Any]) -> Dict[str, Any]:
    return model_runner.run(pd.DataFrame([input_data]))
    