from flask import Flask, render_template, Response, jsonify, request
import settings
import time
import urllib2
import numpy as np
import cv2
import imutils
import datetime
import base64
import subprocess
from flask import send_file, send_from_directory
from flask_analytics import Analytics
from OpenSSL import SSL

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')

# Analytics(app)

log = settings.logging

# app.config['ANALYTICS']['GOOGLE_CLASSIC_ANALYTICS']['ACCOUNT'] = 'UA-115560866-1'


@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/downloadCV')
# def download_resume():
#     return send_file('static/other/adam_jarzebak_cv.pdf', mimetype='pdf', as_attachment=True)



@app.route('/_apiQueryBar')
def api_query_task_range_bar():
    query = request.args.get('apiQ0', "", type=float)
    global alpha

    alpha = query

    reply = "Adjusted alpha channel: {}".format(alpha)

    print (reply)

    return jsonify(result=reply)


# context = SSL.Context(SSL.SSLv23_METHOD)
# context.use_privatekey_file('/etc/letsencrypt/live/adam.sobmonitor.org/privkey.pem')
# context.use_certificate_file('/etc/letsencrypt/live/adam.sobmonitor.org/fullchain.pem')


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=443, threaded=True, ssl_context=('/etc/letsencrypt/live/adam.sobmonitor.org/fullchain.pem','/etc/letsencrypt/live/adam.sobmonitor.org/privkey.pem'))
    app.run(host='0.0.0.0', port=80, threaded=True, debug=False)
    log.debug("Started up analysis app")
