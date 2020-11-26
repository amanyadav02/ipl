from django.shortcuts import render,redirect
from django.contrib import messages
import numpy as np
import pandas as pd
from datetime import datetime
df=pd.read_csv('ipl1.csv')
remove=['mid','venue','batsman','bowler','striker','non-striker']
df.drop(labels=remove,axis=1,inplace=True)
consistent_team=[
        'Kolkata Knight Riders', 'Chennai Super Kings', 'Rajasthan Royals',
       'Mumbai Indians', 'Kings XI Punjab',
       'Royal Challengers Bangalore', 'Delhi Daredevils',
       'Sunrisers Hyderabad'
]
df=df[(df['bat_team'].isin(consistent_team)) & (df['bowl_team'].isin(consistent_team))]
df=df[df['overs']>=5.0]
df['date']=df['date'].apply(lambda x: datetime.strptime(x,'%d-%m-%Y'))
encoded_df=pd.get_dummies(data=df,columns=['bat_team','bowl_team'])
encoded_df=encoded_df[['date',
      'bat_team_Chennai Super Kings', 'bat_team_Delhi Daredevils',
       'bat_team_Kings XI Punjab', 'bat_team_Kolkata Knight Riders',
       'bat_team_Mumbai Indians', 'bat_team_Rajasthan Royals',
       'bat_team_Royal Challengers Bangalore', 'bat_team_Sunrisers Hyderabad',
       'bowl_team_Chennai Super Kings', 'bowl_team_Delhi Daredevils',
       'bowl_team_Kings XI Punjab', 'bowl_team_Kolkata Knight Riders',
       'bowl_team_Mumbai Indians', 'bowl_team_Rajasthan Royals',
       'bowl_team_Royal Challengers Bangalore',
       'bowl_team_Sunrisers Hyderabad','overs','runs', 'wickets', 'runs_last_5', 'wickets_last_5','total']]
X_train=encoded_df.drop(labels='total',axis=1)[encoded_df['date'].dt.year<=2016]
X_test=encoded_df.drop(labels='total',axis=1)[encoded_df['date'].dt.year>=2017]
Y_train=encoded_df[encoded_df['date'].dt.year<=2016]['total'].values
Y_test=encoded_df[encoded_df['date'].dt.year>=2017]['total'].values
X_train.drop(labels='date',axis=True,inplace=True)
X_test.drop(labels='date',axis=True,inplace=True)
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,Y_train)
def main(request):
    if(request.method=='POST'):
        aman=[]
        batting=request.POST.get('batting')
        if(batting=='sunrises'):
            aman+=[1,0,0,0,0,0,0,0]
        elif(batting=='royal'):
            aman+=[0,1,0,0,0,0,0,0]
        elif(batting=='mumbai'):
            aman+=[0,0,1,0,0,0,0,0]
        elif(batting=='chennai'):
            aman+=[0,0,0,1,0,0,0,0]
        elif(batting=='delhi'):
            aman+=[0,0,0,0,1,0,0,0]
        elif(batting=='king'):
            aman+=[0,0,0,0,0,1,0,0]
        elif(batting=='kolkata'):
            aman+=[0,0,0,0,0,0,1,0]
        elif(batting=='rajasthan'):
            aman+=[0,0,0,0,0,0,0,1]
        bowling=request.POST.get('bowling')
        yadav=[]
        if(bowling=='sunrises'):
            aman+=[1,0,0,0,0,0,0,0]
        elif(bowling=='royal'):
            aman+=[0,1,0,0,0,0,0,0]
        elif(bowling=='mumbai'):
            aman+=[0,0,1,0,0,0,0,0]
        elif(bowling=='chennai'):
            aman+=[0,0,0,1,0,0,0,0]
        elif(bowling=='delhi'):
            aman+=[0,0,0,0,1,0,0,0]
        elif(bowling=='king'):
            aman+=[0,0,0,0,0,1,0,0]
        elif(bowling=='kolkata'):
            aman+=[0,0,0,0,0,0,1,0]
        elif(bowling=='rajasthan'):
            aman+=[0,0,0,0,0,0,0,1]
        if(batting==bowling):
            messages.success(request,'batting team and bowling team cannot be same!')
            return redirect('main')
        else:
            over5=request.POST.get('over5')
            aman+=[float(over5)]
            run=request.POST.get('run')
            aman+=[int(run)]
            wicket=request.POST.get('wicket')
            aman+=[int(wicket)]
            run5=request.POST.get('run5')
            aman+=[int(run5)]
            wicket5=request.POST.get('wicket5')
            aman+=[int(wicket5)]
            z=regressor.predict([aman])
            messages.success(request,str(int(z[0])))
            return redirect('main')
    return render(request,'score/main.html')



