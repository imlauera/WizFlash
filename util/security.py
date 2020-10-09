from urllib.parse import urlparse, urljoin
from itsdangerous import URLSafeTimedSerializer
from flask import request
from run import app

ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc
