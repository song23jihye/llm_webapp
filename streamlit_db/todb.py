import joblib #사용할 모델 불러오기
model = joblib.load('/content/drive/MyDrive/steam_trap_project/llm_testmodel.pkl')


import pandas as pd #데이터 불러오기
data = pd.read_csv('/content/drive/MyDrive/steam_trap_project/llm_model/test.csv')
data=data.iloc[:,1:]

pred=model.predict(data) #예측
pred=pd.DataFrame(pred) #df화
final=pd.concat([data,pred],axis=1) #데이터셋 병합
final.columns=['Pregnancies',
 'Glucose',
 'BloodPressure',
 'SkinThickness',
 'Insulin',
 'BMI',
 'DiabetesPedigreeFunction',
 'Age',
 'result']

