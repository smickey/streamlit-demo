import streamlit as st
from streamlit_option_menu import option_menu
from apps import hexagon, home, heatmap  # import your app modules here

#app here

st.set_page_config(page_title="Streamlit Geospatial", layout="wide")

# A dictionary of apps in the format of {"App title": "App icon"}
# More icons can be found here: https://icons.getbootstrap.com

apps = [
    {"func": home.app, "title": "Connect AI", "icon": "cursor"}
    # {"func": heatmap.app, "title": "Heatmap", "icon": "map"},
    # {"func": hexagon.app, "title": "Hexagon", "icon": "hexagon"},
]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        "Connect",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )

    st.sidebar.title("About")
    st.sidebar.info(
        """
        This web [app](https://connect.streamlit.app/) is maintained by the [Connect AI team](https://github.com/khaiyuen/Connect_AI).

        You can follow us on social media:
        [GitHub](https://github.com/khaiyuen/Connect_AI) | [Instagram](https://www.instagram.com/khaiyuen1987) | [LinkedIn](https://sg.linkedin.com/in/khai-yuen-looi-830b4181).

        Streamlit Source: <https://github.com/smickey/streamlit-demo>

        Map Data Source: <https://github.com/khaiyuen/Connect_AI>

        Streamlit template: <https://github.com/giswqs/streamlit-template>

    """
    )

for app in apps:
    if app["title"] == selected:
        app["func"]()
        break
