import yaml
import json
from enum import Enum

class ThemeAppearance(Enum):
    LIGHT = "light"
    DARK = "dark"

VARIANTS = [
    {
        "name": "Jellybeans Pro",
        "filename": "base",
        "appearance": ThemeAppearance.DARK.value
    },
    {
        "name": "Jellybeans Pro Night",
        "filename": "night",
        "appearance": ThemeAppearance.DARK.value
    },
    {
        "name": "Jellybeans Pro Bronze",
        "filename": "bronze",
        "appearance": ThemeAppearance.DARK.value
    },
    {
        "name": "Jellybeans Pro Vibrant",
        "filename": "vibrant",
        "appearance": ThemeAppearance.DARK.value
    },
    {
        "name": "Jellybeans Pro Rizz",
        "filename": "rizz",
        "appearance": ThemeAppearance.LIGHT.value
    },
    {
        "name": "Jellybeans Pro Cream",
        "filename": "cream",
        "appearance": ThemeAppearance.LIGHT.value
    },
    {
        "name": "Jellybeans Pro Punk",
        "filename": "punk",
        "appearance": ThemeAppearance.DARK.value
    },
]


def load_colors(variant):
    with open(f"variants/{variant}.yml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)["colors"]


def jellybeans_theme(name, appearance, colors):
    return {
        "name":
        name,
        "appearance":
        appearance,
        "accents": [
            colors["red"],
            colors["green"],
            colors["yellow"],
            colors["blue"],
            colors["magenta"],
            colors["green"],
            colors["bright_yellow"],
        ],
        "style": {
            "border":
            colors["border"],
            "border.variant":
            colors["border"],
            "border.focused":
            colors["selection"],
            "border.selected":
            colors["selection"],
            "border.transparent":
            "#00000000",
            "border.disabled":
            colors["border_disabled"],
            "elevated_surface.background":
            colors["dark_background"],
            "surface.background":
            colors["background"],
            "background":
            colors["background"],
            "element.background":
            colors["dark_background"],
            "element.hover":
            colors["hover_background"],
            "element.active":
            colors["selection"],
            "element.selected":
            colors["selection"],
            "element.disabled":
            colors["dark_background"],
            "drop_target.background":
            colors["drop_target"],
            "ghost_element.background":
            "#00000000",
            "ghost_element.hover":
            colors["hover_background"],
            "ghost_element.active":
            colors["selection"],
            "ghost_element.selected":
            colors["selection"],
            "ghost_element.disabled":
            colors["dark_background"],
            "text":
            colors["foreground"],
            "text.muted":
            colors["comment"],
            "text.placeholder":
            colors["placeholder"],
            "text.disabled":
            colors["placeholder"],
            "text.accent":
            colors["cyan"],
            "icon":
            colors["foreground"],
            "icon.muted":
            colors["comment"],
            "icon.disabled":
            colors["placeholder"],
            "icon.placeholder":
            colors["comment"],
            "icon.accent":
            colors["cyan"],
            "status_bar.background":
            colors["background"],
            "title_bar.background":
            colors["background"],
            "title_bar.inactive_background":
            colors["dark_background"],
            "toolbar.background":
            colors["background"],
            "tab_bar.background":
            colors["background"],
            "tab.inactive_background":
            colors["dark_background"],
            "tab.active_background":
            colors["background"],
            "search.match_background":
            f"{colors['cyan']}66",
            "panel.background":
            colors["background"],
            "panel.focused_border":
            colors["cyan"],
            "pane.focused_border":
            None,
            "scrollbar.thumb.background":
            colors["scrollbar_thumb"],
            "scrollbar.thumb.hover_background":
            colors["hover_background"],
            "scrollbar.thumb.border":
            colors["hover_background"],
            "scrollbar.track.background":
            "#00000000",
            "scrollbar.track.border":
            colors["dark_background"],
            "editor.foreground":
            colors["foreground"],
            "editor.background":
            colors["background"],
            "editor.gutter.background":
            colors["background"],
            "editor.subheader.background":
            colors["dark_background"],
            "editor.active_line.background":
            f"{colors['dark_background']}bf",
            "editor.highlighted_line.background":
            colors["dark_background"],
            "editor.line_number":
            colors["dark_gray"],
            "editor.active_line_number":
            colors["light_gray"],
            "editor.hover_line_number":
            colors["mid_gray"],
            "editor.invisible":
            "#928474",
            "editor.wrap_guide":
            colors["wrap_guide"],
            "editor.active_wrap_guide":
            colors["active_wrap_guide"],
            "editor.document_highlight.read_background":
            f"{colors['cyan']}1a",
            "editor.document_highlight.write_background":
            "#92847466",
            "terminal.background":
            colors["background"],
            "terminal.foreground":
            colors["foreground"],
            "terminal.bright_foreground":
            colors["foreground"],
            "terminal.dim_foreground":
            colors["background"],
            "terminal.ansi.black":
            colors["black"],
            "terminal.ansi.bright_black":
            colors["bright_black"],
            "terminal.ansi.dim_black":
            colors["dim_black"],
            "terminal.ansi.red":
            colors["red"],
            "terminal.ansi.bright_red":
            colors["bright_red"],
            "terminal.ansi.dim_red":
            colors["dim_red"],
            "terminal.ansi.green":
            colors["green"],
            "terminal.ansi.bright_green":
            colors["bright_green"],
            "terminal.ansi.dim_green":
            colors["dim_green"],
            "terminal.ansi.yellow":
            colors["yellow"],
            "terminal.ansi.bright_yellow":
            colors["bright_yellow"],
            "terminal.ansi.dim_yellow":
            colors["dim_yellow"],
            "terminal.ansi.blue":
            colors["blue"],
            "terminal.ansi.bright_blue":
            colors["bright_blue"],
            "terminal.ansi.dim_blue":
            colors["dim_blue"],
            "terminal.ansi.magenta":
            colors["magenta"],
            "terminal.ansi.bright_magenta":
            colors["bright_magenta"],
            "terminal.ansi.dim_magenta":
            colors["dim_magenta"],
            "terminal.ansi.cyan":
            colors["cyan"],
            "terminal.ansi.bright_cyan":
            colors["bright_cyan"],
            "terminal.ansi.dim_cyan":
            colors["dim_cyan"],
            "terminal.ansi.white":
            colors["white"],
            "terminal.ansi.bright_white":
            colors["bright_white"],
            "terminal.ansi.dim_white":
            colors["dim_white"],
            "link_text.hover":
            colors["link_hover"],
            "version_control_added":
            colors["green"],
            "version_control_modified":
            colors["yellow"],
            "version_control_deleted":
            colors["red"],
            "conflict":
            colors["yellow"],
            "conflict.background":
            colors["warning_bg"],
            "conflict.border":
            colors["warning_border"],
            "created":
            colors["green"],
            "created.background":
            colors["created_bg"],
            "created.border":
            colors["success_border"],
            "deleted":
            colors["red"],
            "deleted.background":
            colors["deleted_bg"],
            "deleted.border":
            colors["error_border"],
            "error":
            colors["red"],
            "error.background":
            colors["error_bg"],
            "error.border":
            colors["error_border"],
            "hidden":
            colors["placeholder"],
            "hidden.background":
            colors["dark_background"],
            "hidden.border":
            colors["border_disabled"],
            "hint":
            colors["hint"],
            "hint.background":
            colors["hint_bg"],
            "hint.border":
            colors["hint_border"],
            "ignored":
            colors["placeholder"],
            "ignored.background":
            colors["dark_background"],
            "ignored.border":
            "#777777",
            "info":
            colors["info"],
            "info.background":
            colors["info_bg"],
            "info.border":
            colors["info_border"],
            "modified":
            colors["yellow"],
            "modified.background":
            colors["modified_bg"],
            "modified.border":
            colors["warning_border"],
            "predictive":
            colors["predictive"],
            "predictive.background":
            colors["predictive_bg"],
            "predictive.border":
            colors["predictive_border"],
            "renamed":
            colors["cyan"],
            "renamed.background":
            colors["renamed_bg"],
            "renamed.border":
            colors["info_border"],
            "success":
            colors["green"],
            "success.background":
            colors["success_bg"],
            "success.border":
            colors["success_border"],
            "unreachable":
            colors["gray"],
            "unreachable.background":
            colors["dark_background"],
            "unreachable.border":
            "#777777",
            "warning":
            colors["yellow"],
            "warning.background":
            colors["warning_bg"],
            "warning.border":
            colors["warning_border"],
            "players": [{
                "cursor": c,
                "background": c,
                "selection": f"{c}3d"
            } for c in [
                colors["cyan"],
                colors["magenta"],
                colors["bright_yellow"],
                colors["red"],
                colors["green"],
                colors["yellow"],
                colors["blue"],
                colors["green"],
            ]],
            "syntax": {
                "attribute": {
                    "color": colors["cyan"]
                },
                "namespace": {
                    "color": colors["cyan"]
                },
                "boolean": {
                    "color": colors["red"]
                },
                "comment": {
                    "color": colors["comment"],
                    "font_style": "italic"
                },
                "comment.doc": {
                    "color": colors["comment_doc"]
                },
                "constant": {
                    "color": colors["red"]
                },
                "constructor": {
                    "color": colors["cyan"]
                },
                "embedded": {
                    "color": colors["green"]
                },
                "emphasis": {
                    "color": colors["cyan"]
                },
                "emphasis.strong": {
                    "color": colors["cyan"],
                    "font_weight": 700
                },
                "enum": {
                    "color": colors["bright_yellow"]
                },
                "function": {
                    "color": colors["yellow"]
                },
                "function.builtin": {
                    "color": colors["red"]
                },
                "hint": {
                    "color": colors["hint"],
                    "font_weight": 700
                },
                "keyword": {
                    "color": colors["blue"]
                },
                "label": {
                    "color": colors["cyan"]
                },
                "link_text": {
                    "color": colors["green"],
                    "font_style": "italic"
                },
                "link_uri": {
                    "color": colors["magenta"]
                },
                "number": {
                    "color": colors["red"]
                },
                "operator": {
                    "color": colors["cyan"]
                },
                "predictive": {
                    "color": colors["predictive"],
                    "font_style": "italic"
                },
                "preproc": {
                    "color": colors["foreground"]
                },
                "primary": {
                    "color": colors["foreground"]
                },
                "property": {
                    "color": colors["foreground"]
                },
                "punctuation": {
                    "color": colors["foreground"]
                },
                "punctuation.bracket": {
                    "color": colors["comment"]
                },
                "punctuation.delimiter": {
                    "color": colors["foreground"]
                },
                "punctuation.list_marker": {
                    "color": colors["foreground"]
                },
                "punctuation.special": {
                    "color": colors["foreground"]
                },
                "string": {
                    "color": colors["green"]
                },
                "string.escape": {
                    "color": colors["string_escape"]
                },
                "string.regex": {
                    "color": colors["string_regex"]
                },
                "string.special": {
                    "color": colors["string_special"]
                },
                "string.special.symbol": {
                    "color": colors["symbol"]
                },
                "tag": {
                    "color": colors["green"]
                },
                "text.literal": {
                    "color": colors["cyan"]
                },
                "title": {
                    "color": colors["yellow"],
                    "font_weight": 700
                },
                "type": {
                    "color": colors["bright_yellow"]
                },
                "variable": {
                    "color": colors["foreground"]
                },
                "variant": {
                    "color": colors["cyan"]
                },
            },
        },
    }


def main():
    theme_root = {
        "$schema": "https://zed.dev/schema/themes/v0.2.0.json",
        "name": "Jellybeans Pro",
        "author": "Daniil Shilo",
        "themes": [],
    }

    for variant in VARIANTS:
        colors = load_colors(variant["filename"])
        theme = jellybeans_theme(variant['name'], variant['appearance'], colors)
        theme_root["themes"].append(theme)

    with open("themes/jellybeans-pro.json", "w", encoding="utf-8") as f:
        json.dump(theme_root, f, indent=2)
    print("✅ jellybeans.json has been generated")


if __name__ == "__main__":
    main()
