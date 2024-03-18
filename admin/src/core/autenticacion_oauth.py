from flask_oauthlib.client import OAuth

google_client_id = ""
google_client_secret = ""
google_redirect_uri = ""


oauth = OAuth()
google = oauth.remote_app(
    "google",
    consumer_key=google_client_id,
    consumer_secret=google_client_secret,
    request_token_params={
        "scope": "email profile",
    },
    base_url="https://www.googleapis.com/oauth2/v1/",
    request_token_url=None,
    access_token_method="POST",
    access_token_url="https://accounts.google.com/o/oauth2/token",
    authorize_url="https://accounts.google.com/o/oauth2/auth",
)


def init_app(app):
    oauth.init_app(app)
