import streamlit as st
import streamlit.components.v1 as components

# Load your HTML file
with open("index.html", "r") as file:
    html_content = file.read()

# Add the CSS and JS links if they're not in the HTML file
#html_content = html_content.replace(
    '</head>', 
    '<link rel="stylesheet" type="text/css" href="styles.css">' +
    '<script src="script.js"></script>' +
    '</head>'
)
#

# Render the HTML in Streamlit
components.html(html_content, height=600)
