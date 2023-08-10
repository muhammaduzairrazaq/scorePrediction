import pickle
import pandas as pd
import numpy as np





pipe = pickle.load(open('pipe.pkl','rb'))

teams= ['India', 'Pakistan', 'Bangladesh', 'West Indies', 'England',
       'Afghanistan', 'Sri Lanka', 'South Africa', 'Australia',
       'New Zealand'] 

cities =['Durban', 'Trinidad', 'Lahore', 'Lauderhill', 'Nottingham',
       'Mirpur', 'Cardiff', 'Melbourne', 'Nagpur', 'Pallekele',
       'Southampton', 'Barbados', 'Johannesburg', 'Cape Town',
       'Mount Maunganui', 'Chandigarh', 'Delhi', 'Centurion',
       'Manchester', 'Sydney', 'London', 'St Lucia', 'Christchurch',
       'Wellington', 'Auckland', 'Colombo', 'Dubai', 'Abu Dhabi',
       'Adelaide', 'Mumbai', 'Hamilton', 'Kolkata', 'Chittagong',
       'Bangalore', 'St Kitts']

teams.sort()
cities.sort()




def predict_score(current_score,overs,wicket,last_five, batting_team,bowling_team,city):

    balls_left = 120 - (overs*6)
    wickets = 10-wicket
    crr = current_score / overs
    
    test_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':city, 'current_score':[current_score],'balls_left':[balls_left],'wickets_left':[wickets],'crr':[crr], 'last_five':[last_five]})
    pred_score = pipe.predict(test_df)
    return (int(pred_score))


