from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np


model = joblib.load('house_price_model.pkl')


app = FastAPI()


app.add_middleware(
CORSMiddleware,
allow_origins=["*"],
allow_methods=["*"],
allow_headers=["*"],
)


class HouseData(BaseModel):
luas_bangunan: float


@app.post("/predict")
def predict_price(data: HouseData):
input_data = np.array([[data.luas_bangunan]])
prediction = model.predict(input_data)[0]
return {"harga_rumah": prediction}
