import requests

def check_facebook_token_validity(access_token):
    url = f"https://graph.facebook.com/me?access_token={access_token}"
    response = requests.get(url)

    if response.status_code == 200:
        return True
    else:
        return False

access_token = "EAAAAUaZA8jlABALr8uJ89wElzWZAPDwWR9545eVEZC6FxSZBkZByvTkup8Ya1sKNorsouKPigV91FxIgJIeFBIpeKuK6uK6Um4ZBWJHrFC27HqfFOPHZClMZCeoFPR6UZAgHr26gRclbWZAjCFRZCygglNFo02TMUfX5O0BmYzilycG2nAbyOXfyfPnkmFkF4ZCste4ZD"
is_valid = check_facebook_token_validity(access_token)

if is_valid:
    print("Facebook access token is valid.")
else:
    print("Facebook access token is not valid.")