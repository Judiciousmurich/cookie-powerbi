import pandas as pd
from fbprophet import Prophet

# Load the cleaned sales data
data = pd.read_csv('../data/transformed/kevin_cookie_sales_cleaned.csv')

# Prepare the data for Prophet (ensure the columns are named correctly)
data = data.rename(columns={'Sale_Date': 'ds', 'Sales': 'y'})  # Prophet requires 'ds' for dates and 'y' for values

# Instantiate and fit the model
model = Prophet()
model.fit(data)

# Make future predictions (e.g., 30 days ahead)
future = model.make_future_dataframe(data, periods=30)
forecast = model.predict(future)

# Plot the forecast (you can save this as an image or use it in a report)
model.plot(forecast)

# Save the forecasted data to a CSV
forecast.to_csv('../data/transformed/forecasted_sales.csv', index=False)
print("Sales forecast generated and saved.")
