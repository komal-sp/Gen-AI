import requests
import os
from datetime import datetime

GENDER = "female"
WEIGHT_KG = "49"
HEIGHT_CM = "154"
AGE = "25"

WORKOUT_API_KEY = os.environ["WORKOUT_API_KEY"]
WORKOUT_APP_ID = os.environ.get("WORKOUT_APP_ID")

WORKOUT_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

workout_headers = {
    "x-app-id": WORKOUT_APP_ID,
    "x-app-key": WORKOUT_API_KEY,
    "Content-Type": "application/json",
}

workout_text = input("Tell me which exercises you did: ")

workout_parameters = {
    "query": workout_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

workout_response = requests.post(url=WORKOUT_ENDPOINT, json=workout_parameters, headers=workout_headers)
workout_response.raise_for_status()
result = workout_response.json()
print(result)
# {'exercises': [{'tag_id': 100, 'user_input': 'walking', 'duration_min': 5, 'met': 3.5, 'nf_calories': 14.29,
# 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/100_highres.jpg',
# 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/100_thumb.jpg', 'is_user_uploaded': False},
# 'compendium_code': 17190, 'name': 'walking', 'description': None, 'benefits': None}]}

sheet_endpoint = "https://api.sheety.co/b6c82eb63975bd54b4f210fce7957334/workoutTracking/workouts"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": datetime.today().strftime("%d/%m/%Y"),
            "time": datetime.today().strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }


# No Authentication
# sheet_response = requests.post(
#     sheet_endpoint,
#     json=sheet_inputs,
#     headers=bearer_headers
# )

# USERNAME = "Komal"
# PASSWORD = "workout@876"
#
# # Basic Authentication
# sheet_response = requests.post(
#   sheet_endpoint,
#   json=sheet_inputs,
#   auth=(USERNAME, PASSWORD,)
# )

# Bearer Token Authentication
bearer_headers = {
    "Authorization": "Bearer workout@876"
}
sheet_response = requests.post(
    sheet_endpoint,
    json=sheet_inputs,
    headers=bearer_headers
)

print(sheet_response.json())
