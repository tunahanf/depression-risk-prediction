import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv("Depression.csv")
ohe = OneHotEncoder(drop="first")

# -- PREPROCESSING --

xd = ohe.fit_transform(df[["Gender", "Sleep Duration", "Dietary Habits", "Have you ever had suicidal thoughts ?", "Family History of Mental Illness", "Depression"]]).toarray()
xd = pd.DataFrame(xd)

xd.columns=[ohe.get_feature_names_out()]
df[xd.columns] = xd
df = df.drop(columns=["Gender", "Sleep Duration", "Dietary Habits", "Have you ever had suicidal thoughts ?", "Family History of Mental Illness", "Depression"])
df.columns = ["Age", "AcaPress", "StudSatis", "StudHour", "FinanStress", "GenderMale", "SleepDur7", "SleepDur5", "SleepDur8", "DietMod", "DietUn", "SuicYes", "MentalYes", "DepressYes"] # Renaming Columns

# -- TRAINING MODEL -- 

y = df["DepressYes"]
x = df.drop("DepressYes", axis=1)

rf = RandomForestClassifier(n_estimators=200)
x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=.6, random_state=60)
model = rf.fit(x_train, y_train)

# -- GET ANSWERS FROM USER -- 

questions = ["Age : ", "Academic Pressure (1-5) : ", "Study Satisfaction (1-5) : ", "Study Hour : ", "Financal Stress (1-5) : ", "Gender : ", "Sleep Duration : ",
             "Dietary Habits (Moderate, Unhealthy, Healthy) : ", "Have you ever had suicidal thoughts?(1: Yes, 0: No) : ", "Family History of Mental Illness?(1: Yes, 0: No) : "]

answerList = []

for question in questions:
    answer = input(f"{question}")
    if question == "Gender":
        if answer == "Male":
            answerList.extend([1])
        elif answer == "Female":
            answerList.extend([0])
    
    elif question == "Sleep Duration":
        # Mevcut Sleep Duration kodunuz
        if int(answer) <= 5:
            answerList.extend([0, 1, 0])
        elif int(answer) > 8:
            answerList.extend([0, 0, 1])
        elif int(answer) in [7, 8]:
            answerList.extend([1, 0, 0])
        else:
            answerList.extend([0, 0, 0])
    
    elif question == "Dietary Habits (Moderate, Unhealthy, Healthy)":
        # Mevcut Dietary Habits kodunuz
        if answer == "Moderate":
            answerList.extend([1, 0])
        elif answer == "Unhealthy":
            answerList.extend([0, 1])
        else:
            answerList.extend([0, 0])
    else:
        answerList.extend([answer])


answerList = list(map(int, answerList))
output = model.predict([answerList])
if output == np.array([0]):
    print("You have LOW RISK of DEPRESSION")
else:
    print("You have HIGH RISK of DEPRESSION")
