# Neuroflow

Create a web REST application with a '/mood' endpoint, which when POSTed to persists the submitted mood value.

Add the ability for users to login.

Create a '/mood' endpoint with a GET method, returning all values submitted by the logged-in user.

Add to the body of the response for the ‘/mood’ endpoint the length of their current "streak".
- A user is on a “streak” if that user has submitted at least 1 mood rating for each consecutive day of that streak.
- For example, if on March 1st, March 2nd, March 3rd, and March 5th the user entered mood ratings, a 3-day streak will apply to the March 3rd rating and the streak will reset to a 1-day streak for the March 5th rating.
