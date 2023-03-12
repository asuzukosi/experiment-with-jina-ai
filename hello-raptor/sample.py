import pandas as pd
from raptor import data_source, StreamingConfig,  feature, aggregation, AggregationFunction, Context, model, freshness, TrainingContext
from typing_extensions import TypedDict


@data_source(
  training_data=pd.read_csv(
    'https://gist.githubusercontent.com/AlmogBaku/8be77c2236836177b8e54fa8217411f2/raw/hello_world_transactions.csv'),
  production_config=StreamingConfig()
)
class BankTransaction(TypedDict):
  customer_id: str
  amount: float
  timestamp: str


# Define features 🧪
@feature(keys='customer_id', data_source=BankTransaction)
@aggregation(function=AggregationFunction.Sum, over='10h', granularity='1h')
def total_spend(this_row: BankTransaction, ctx: Context) -> float:
  """total spend by a customer in the last hour"""
  return this_row['amount']


@feature(keys='customer_id', data_source=BankTransaction)
@freshness(max_age='5h', max_stale='1d')
def amount(this_row: BankTransaction, ctx: Context) -> float:
  """total spend by a customer in the last hour"""
  return this_row['amount']


# Train the model 🤓
@model(
  keys='customer_id',
  input_features=['total_spend+sum'],
  input_labels=[amount],
  model_framework='sklearn',
  model_server='sagemaker-ack',
)
@freshness(max_age='1h', max_stale='100h')
def amount_prediction(ctx: TrainingContext):
  from sklearn.linear_model import LinearRegression
  df = ctx.features_and_labels()
  trainer = LinearRegression()
  trainer.fit(df[ctx.input_features], df[ctx.input_labels])
  return trainer


amount_prediction.export()  # Export to production 🎉