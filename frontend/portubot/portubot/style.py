# style.py
import reflex as rx

# Brazilian color palette
colors = {
    "green": "#009739",  # Brazil flag green
    "yellow": "#FEDD00",  # Brazil flag yellow
    "blue": "#012169",   # Brazil flag blue (darker for contrast)
    "white": "#FFFFFF",
    "amazon_green": "#3B7A57",  # Amazon rainforest green
    "carnival_purple": "#6A3093",  # Carnival purple
    "sunset_orange": "#FF7F50",  # Tropical sunset orange
}

# Common styles for questions and answers with Brazilian flair
shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
chat_margin = "20%"
message_style = dict(
    padding="1em",
    border_radius="8px",  # Slightly more rounded for a softer look
    margin_y="0.5em",
    box_shadow=shadow,
    max_width="30em",
    display="inline-block",
    color=colors["blue"],  # Dark blue text for better readability
)

# Question style - inspired by Brazil's green
question_style = message_style | dict(
    margin_left=chat_margin,
    background_color=colors["green"],
    color=colors["white"],  # White text for contrast
    border_left=f"4px solid {colors['yellow']}",  # Yellow accent border
)

# Answer style - inspired by Brazil's yellow
answer_style = message_style | dict(
    margin_right=chat_margin,
    background_color=colors["yellow"],
    border_right=f"4px solid {colors['green']}",  # Green accent border
)

# Action bar with tropical colors
input_style = dict(
    border_width="1px",
    border_color=colors["green"],
    padding="0.7em",  # Slightly more padding
    box_shadow=shadow,
    width="350px",
    border_radius="20px",  # Rounded input field
    _focus={"border_color": colors["blue"]},  # Blue focus effect
)

button_style = dict(
    background_color=colors["blue"],
    color=colors["white"],
    box_shadow=shadow,
    border_radius="20px",  # Rounded button
    padding="0.7em 1.5em",
    _hover={
        "background_color": colors["amazon_green"],  # Amazon green on hover
        "transform": "scale(1.05)",  # Slight grow effect
    },
    transition="all 0.3s ease",  # Smooth transition
)

background_style = dict(
    background_color="white",  # Pure white background
    min_height="100vh",
    padding="2em",
)

# Carnival-inspired chat container
chat_container_style = dict(
    background_color=colors["white"],
    border_radius="15px",
    padding="2em",
    box_shadow=f"0 4px 20px {colors['carnival_purple']}",
    max_width="800px",
    margin="auto",
    border=f"2px solid {colors['yellow']}",
)