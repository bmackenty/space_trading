from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
from textual.widgets import Static

class SpaceTrader(App):
    """Space Trader!"""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    CSS_PATH = "horizontal_layout.tcss" 

    def compose(self) -> ComposeResult:
        yield Static("One", classes="box")
        yield Static("Two [b](column-span: 2 and row-span: 2)", classes="box", id="two")
    
    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = SpaceTrader()
    app.run()
