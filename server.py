from flask import Flask, jsonify, json, abort, request, make_response, url_for
from flask_httpauth import HTTPBasicAuth
import datetime

app = Flask(__name__, static_url_path = "")
auth = HTTPBasicAuth()

validMoods = ["angry", "anxious", "happy" "sad", "tired"]

def streak_calculation(moods):
    dateList = []
    for obj in moods:
        dateList += list(obj.keys()) 
    justDays = []
    [justDays.append(x) for x in dateList if x not in justDays] # reducing mulitple entries per day to one
    sortedDateList = sorted(justDays)
    current_date = sortedDateList[0]
    current_streak = 1
    for date in sortedDateList:
        if date - current_date == 1:
            current_streak += 1
            current_date = date
        else:
            current_date = date
            current_streak = 1
    return current_streak



@auth.get_password
def get_password(username):
    if username == 'adminUsername':
        return 'adminPassword'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify( { 'error': 'Unauthorized access' } ), 403)
    # return 403 instead of 401 to prevent browsers from displaying the default auth dialog
    
@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

moods = []
    
@app.route('/mood', methods = ['GET'])
@auth.login_required
def get_moods():
    return jsonify({"moods": moods}), 201


@app.route('/mood', methods = ['POST'])
@auth.login_required
def create_mood():
    mood = request.json.get('mood')
    if not request.json or mood not in validMoods:
        abort(400)
    newMood = {
        datetime.datetime.now().toordinal():mood
    }
    moods.append(newMood)
    return jsonify({'current_streak': streak_calculation(moods)}), 201 

    
if __name__ == '__main__':
    app.run(debug = False)