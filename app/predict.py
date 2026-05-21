import joblib
model = joblib.load("models/model.pkl")
hours = [[6]]

predictions = model.predict(hours)


print("predicated marks:", predictions[0])