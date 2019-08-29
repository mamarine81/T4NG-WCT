from flask import Flask, request, abort, jsonify
from wct_app.config.wct_config import WCT_VERSION, WCT_SECRET_SAUCE

APP = Flask(__name__)

class Widgetizer:
    def __init__(self, widget_material):
        self.widget_material = str(widget_material)
        self.secret_sauce = int(WCT_SECRET_SAUCE)
        self.widget = ''.join(['(ಠ_ಠ){}(ಠ_ಠ)\n'.format(self.widget_material) \
        for _ in range(self.secret_sauce)])

    def save_widget(self):

        with open('widget.store', 'a') as outfile:
            outfile.write('\n\n{}'.format(self.widget))

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
