from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# Load EDE-Q 6.0 data from a CSV file
data = pd.read_csv(r"C:\Users\Eliza\.vscode\anorexiav2\safahdhdj copy.xlsx")

# Preprocess data, such as imputing missing values or scaling features

# Extract features and target variable from data
X = data.drop(['SignPost'], axis=1)
y = data['SignPost']

# Train logistic regression model on entire dataset
model = LogisticRegression()
model.fit(X, y)

# Define chatbot route
@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    if request.method == 'GET':
        # Render chatbot template with first question
        return render_template('chatbot.html', question='Have you been deliberately trying to limit the amount of food you eat to influence your shape or weight (whether or not you have succeeded)?')
    elif request.method == 'POST':
        # Get user's response to current question
        response = request.form['response']

        # Store user's responses in a list or array
        responses = [response]

        # Ask next question based on user's previous response
        if response == 'Yes':
            question = 'Do you avoid eating certain foods or food groups?'
        elif response == 'No':
            question = 'Do you have a sense of loss of control when you eat?'
        else:
            question = 'Sorry, I didn\'t understand your response. Please answer with "Yes" or "No".'

        # If all questions have been asked, make prediction based on user's responses
        if len(responses) == 4:
            # Convert user's responses to a DataFrame
            df = pd.DataFrame(responses, columns=X.columns)

            # Make prediction based on user's responses
            prediction = model.predict(df)

            # Provide user with feedback on prediction
            if prediction == 1:
                feedback = 'Based on your responses, it appears that you may be at risk for an eating disorder. Please seek professional help if you have concerns about your eating habits.'
            else:
                feedback ='None'
