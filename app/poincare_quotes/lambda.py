from apig_wsgi import make_lambda_handler

from quotes.wsgi import application

lambda_handler = make_lambda_handler(application)
