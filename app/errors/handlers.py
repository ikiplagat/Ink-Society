from flask import Blueprint,render_template

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('errors/fourOwfour.html'),404

@errors.app_errorhandler(403)
def four_Ow_three(error):
    '''
    Function to render the 403 error page
    '''
    return render_template('errors/fourOwthree.html'),403