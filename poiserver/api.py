import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('api', __name__, url_prefix='/api')

def ally(lat, lon):
    # takes location
    # return dictionary of points of interest
    pass

def josiah(ally_info):
    # takes dictionary of points of interest
    # gets more info from yelp
    # package together so Seth can be lazy
    pass

@bp.route('/<float:lat>/<float:lon>', methods=('GET', 'POST'))
def info(lat, lon):
    print(lat, lon)
    #return josiah(ally(lat, lon))

    return {
        'city': 'None',
        'mountain': 'Mnt. Olympia',
        'river': 'Your eyes'
    }