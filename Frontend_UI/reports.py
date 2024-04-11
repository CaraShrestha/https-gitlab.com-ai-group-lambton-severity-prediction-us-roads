import streamlit as st
def display_reports():
    # Set the Streamlit theme to be white
    st.header("Reports")
    # Use CSS to adjust the width of the iframe
    st.markdown(
        """
        <style>
            .reportview-container .main .block-container {
                max-width: 100%;
            }
            .tableau-iframe {
                width: 100%;
                height: 1000px;
                border: none;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    # Embed the report using an iframe
    st.markdown(
        """
        <iframe class="tableau-iframe" src="https://public.tableau.com/views/Severity_in_Traffic_Flow_in_US/SeverityofCarAccidentsinTrafficFlowintheUSfrom2016-2023?:language=en-US&publish=yes&:sid=&:display_count=n&:origin=viz_share_link?:showVizHome=no&:embed=true" width="1000" height="600" frameborder="0"></iframe>
        """,
        unsafe_allow_html=True
    )