from flask import Flask, request, abort, jsonify
from wct_app.config.wct_config import WCT_VERSION
from wct_app.lib.widgetizer.widgetizer import Widgetizer


APP = Flask(__name__)

@APP.route('/api/v0/widgetize', methods=['POST'])
def widgetize():

    to_widgetize = request.get_json(force=True)

    if not to_widgetize.get('widget_material', None):
        abort(400)

    widgetized = Widgetizer(to_widgetize['widget_material'])

    widgetized.save_widget()

    return jsonify({
        'widget':widgetized.widget,
        'wct_version': WCT_VERSION
        })
