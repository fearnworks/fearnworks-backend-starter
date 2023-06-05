class StyleManager:
    def __init__(self, theme="light"):
        self.theme = theme
        self.colors = {
            "background": "#FFFFFF",
            "text": "#000000",
            "primary": "#007ACC",
            "secondary": "#6C757D",
            "success": "#28A745",
            "info": "#17A2B8",
            "warning": "#FFC107",
            "danger": "#DC3545",
        }

    def get_color(self, color_name):
        return self.colors[color_name]

    def get_theme(self):
        return self.theme

    def set_theme(self, theme):
        self.theme = theme
        # Update colors based on new theme
        if theme == "light":
            self.colors = {
                "background": "#FFFFFF",
                "text": "#000000",
                "primary": "#007ACC",
                "secondary": "#6C757D",
                "success": "#28A745",
                "info": "#17A2B8",
                "warning": "#FFC107",
                "danger": "#DC3545",
            }
        elif theme == "dark":
            self.colors = {
                "background": "#1E1E1E",
                "text": "#FFFFFF",
                "primary": "#0DB9D7",
                "secondary": "#6C757D",
                "success": "#3EBD93",
                "info": "#17A2B8",
                "warning": "#FFC107",
                "danger": "#DC3545",
            }
        else:
            raise ValueError("Invalid theme name")

    def get_layout(self):
        return {
            "plot_bgcolor": self.colors["background"],
            "paper_bgcolor": self.colors["background"],
            "font": {"color": self.colors["text"]},
        }

    def get_styles(self):
        styles = {
            ".page-3a": {
                "color": self.colors["text"],
                "font-size": "16px",
                "font-weight": "bold",
                "margin-bottom": "20px",
            },
            ".page-3b": {
                "color": self.colors["text"],
                "font-size": "14px",
                "margin-bottom": "10px",
            },
            ".page-3c": {
                "color": self.colors["text"],
                "font-size": "14px",
                "margin-bottom": "10px",
            },
            ".page-3d": {
                "color": self.colors["text"],
                "font-size": "14px",
                "margin-bottom": "10px",
            },
            ".page-3e": {
                "color": self.colors["text"],
                "font-size": "14px",
                "margin-bottom": "10px",
            },
            ".page-3f": {
                "color": self.colors["text"],
                "font-size": "14px",
                "margin-bottom": "10px",
            },
            ".page-3g": {
                "border-left-color": self.colors["primary"],
                "margin-top": "20px",
                "border-left-width": "7px",
            },
            ".page-3h": {
                "color": self.colors["primary"],
            },
            ".page-3i": {
                "background-color": "#F8F8FF",
                "padding-top": "10px",
                "padding-bottom": "10px",
                "padding-right": "20px",
            },
            ".page-3j": {
                "margin-left": "250px",
                "margin-bottom": "15px",
                "width": "400px",
            },
            ".page-3k": {
                "font-size": "11px",
            },
            ".page-3l": {
                "position": "relative",
                "margin-top": "40px",
                "margin-left": "30px",
            },
            ".page-3m": {
                "height": "250px",
            },
            ".page-5": {
                "border-left": "5px",
                "border-left-style": "solid",
                "border-left-color": self.colors["primary"],
                "padding": "20px",
                "border-left-width": "7px",
            },
        }
        return styles