Free up the `Alt` key for your own shortcuts by disabling the main menu `Alt+Letter` navigation shortcuts.

## Installation
1. Copy the `UnbindAltShortcuts` folder and `UnbindAltShortcuts.desktop` to the `pykrita` directory found in your **Krita resources folder**.
2. Start Krita and enable the plugin at: `Settings > Configure Krita... > Python Plugin Manager`
3. Restart Krita.
4. 
## Compatibility

This plugin was last tested on Krita 5.2.2. It should keep working until Krita's next major release at the very least.

## Known Issues

The main menu shortcuts will be briefly active when starting Krita or opening a new window. You might even spot it from the underlined words.

That happens because the menu entries don't exist while the window is being created, only after, so they can be only altered when the window is already visible.
