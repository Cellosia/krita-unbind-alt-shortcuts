from krita import Krita, Extension


class UnbindAltShortcutsExtension(Extension):
    """ Register Unbind Alt Shortcut Extension """
    def __init__(self, parent):
        """ Initialize extension """
        super().__init__(parent)
        self.app = Krita.instance()

        # Init listener
        appNotifier = self.app.notifier()
        appNotifier.setActive(True)
        # Run every time a new window is created.
        #   Can't be while windows are still being created because
        #   they don't have a menuWidget with actions yet.
        appNotifier.windowCreated.connect(self.window_ready)

    def setup(self):
        pass

    def createActions(self, window):
        pass

    def window_ready(self):
        """ Window was created and is shown to user """
        # qwin = self.new_window
        qwin = self.app.activeWindow().qwindow()

        # -- Disable main menu shortcuts by removing "&" auto-shortcuts
        actions = qwin.menuWidget().actions()
        for action in actions:
            action.setText(action.text().replace("&", ""))


# Create extension
Krita.instance().addExtension(UnbindAltShortcutsExtension(Krita.instance()))
