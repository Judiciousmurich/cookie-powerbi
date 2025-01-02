import pandas as pd
from fbprophet import Prophet

# Load the cleaned sales data
data = pd.read_csv('../data/transformed/kevin_cookie_sales_cleaned.csv')


data = data.rename(columns={'Sale_Date': 'ds', 'Sales': 'y'})  


model = Prophet()
model.fit(data)


future = model.make_future_dataframe(data, periods=30)
forecast = model.predict(future)

model.plot(forecast)

forecast.to_csv('../data/transformed/forecasted_sales.csv', index=False)
print("Sales forecast generated and saved.")
