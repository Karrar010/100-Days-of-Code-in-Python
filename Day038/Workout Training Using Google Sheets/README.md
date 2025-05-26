# Workout Tracker

## Objective
Build an exercise tracking app using natural language processing and Google sheets.

## FAQ Sheety: Insufficient Permission

Sheety needs permission to access your Google Sheet. When you sign into Sheety you probably forgot to give it permission. Sign out of Sheety and sign in again. Also, go to your Google Account -> Security -> Third Party Apps with Account Access. Check that you see Sheety listed there.

## FAQ Sheety: Bad Request. The JSON Payload should be inside a root property called "X"

Your Google sheet's name should be plural – if it isn’t then Sheety will still expect it to be camelCase plural in the API endpoint. i.e. if your sheet is named "My Workouts", then you should use "myWorkouts" in your endpoint.
The Project name in the endpoint must also be camelCase.
The name you use for the primary key in the API call should be the camelCase singular version of the sheet name. i.e. if your sheet is named "My Workouts", then you should use "myWorkout" in your API dictionary. You may also need to refresh the API page on Sheety.
