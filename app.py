import streamlit as st
from starting_point import get_output


# @app.route('/')
def welcome():
    return "Welcome All"


def main():
    html_temp = """
    <div style="background-color:grey;padding:10px">
    <h2 style="color:white;text-align:center;">Code AutoCompleter App {just for fun}) </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    code = st.text_input("start entering some code....   ")
    result=None
    if st.button("get autocompleted suggestions!"):
        result = get_output(code)
    st.success(' output  ')
    # with st.echo():
    st.text(result)

if __name__ == '__main__':
    main()
