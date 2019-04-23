from flask import render_template
from . import main

@main.errorhandler(404)
def four_ow_four(error):
    '''
    View function to display the error page
    '''
    return render_template('four_ow_four.html') , 404