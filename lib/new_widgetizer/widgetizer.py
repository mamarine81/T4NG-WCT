from wct_app.config.wct_config import WCT_SECRET_SAUCE, PATH_TO_DATA_FILE

class NewWidgetizer:
    def __init__(self, widget_material):
        self.widget_material = str(widget_material)
        self.secret_sauce = int(WCT_SECRET_SAUCE)
        self.widget = ''.join(['(ಠ_ಠ){}(ಠ_ಠ)\n'.format(self.widget_material) \
        for _ in range(self.secret_sauce)])

    def save_widget(self):
        with open('{}/widget.store'.format(PATH_TO_DATA_FILE), 'a') as outfile:
            outfile.write('\n\n{}'.format(self.widget))

    def foo(self):
        var12 = var5(arg2, arg1)
        if arg1 < arg2:
            var17 = class5()
        else:
            var17 = class7()
        for var18 in range(15):
            var19 = var17.func6
            var19(var18, arg2)

    def bar(self, arg15, arg16):
        return 0
