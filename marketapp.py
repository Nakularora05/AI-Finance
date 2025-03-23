from stock_utility_handler import StockAPI, StockAnalyzer
from ai_insights_handler import AIInsights

import streamlit as st
import os
import tempfile

# Initialize session state variables
if 'page' not in st.session_state:
    st.session_state.page = "page1"
    st.session_state.ticker = "RELIANCE"
    st.session_state.market = "BSE"
    st.session_state.image_path = ""
    st.session_state.ai_insights = ""
    st.session_state.internal_results_available = False


# Page 1: Input Page
def page1():
    st.title('Stock AI Agent')

    col1, col2 = st.columns(2)
    with col1:
        st.session_state.ticker = st.text_input("Enter Stock Ticker Symbol", value=st.session_state.ticker, key="ticker_input")
    with col2:
        st.session_state.market = st.selectbox("Select Market", ["BSE", "NASDAQ"], index=["BSE", "NASDAQ"].index(st.session_state.market), key="market_input")

    st.sidebar.header("About")
    st.sidebar.write("This is a stock analysis platform powered by AI insights.")

    st.markdown("---")

    if st.button('Submit'):
        st.session_state.page = "page2"
        st.session_state.internal_results_available = False
        st.rerun()


# Page 2: Analysis Page
def page2():
    st.title(f"Analysis for {st.session_state.ticker} ({st.session_state.market})")

    stock = st.session_state.ticker
    market = st.session_state.market

    if not st.session_state.internal_results_available:
        with st.spinner('Analyzing... Please wait...'):
            # ✅ Use a safe temporary directory for image storage
            temp_dir = tempfile.gettempdir()
            image_path = os.path.join(temp_dir, f"{market}_{stock}.png")
            st.session_state.image_path = image_path

            try:
                # Initialize API objects
                stock_api_obj = StockAPI("1UJ6ACYM0P4MHORZ")
                stock_analyzer_obj = StockAnalyzer()
                ai_insights_obj = AIInsights("AIzaSyAVi1v80vt41mTjZED6BaMs5-74HKFkSk0")

                # Fetch stock data
                market_data = stock_api_obj.get_stock_info(stock, market)

                # Convert JSON to DataFrame
                df = stock_analyzer_obj.json_to_dataframe(market_data, stock, market)

                # Generate stock plot
                stock_analyzer_obj.plot_stock_data(df, stock, market, image_path)

                # Get AI insights
                response = ai_insights_obj.get_ai_insights(image_path, stock, market)

                # Extract insights from AI response
                st.session_state.ai_insights = ""
                for candidate in response.candidates:
                    for part in candidate.content.parts:
                        print(part.text)
                        st.session_state.ai_insights += part.text

                st.session_state.internal_results_available = True

            except Exception as e:
                st.error(f"An error occurred: {e}")
                return

    # Display results if analysis is complete
    if st.session_state.internal_results_available:
        st.subheader("Chart Analysis")
        st.image(st.session_state.image_path, caption=f"{stock} Chart", use_column_width=True)

        st.subheader("AI Insights")
        st.write(st.session_state.ai_insights)

        if st.button("Back"):
            st.session_state.page = "page1"
            st.session_state.internal_results_available = False
            st.rerun()


# Route between pages
if st.session_state.page == "page1":
    page1()
elif st.session_state.page == "page2":
    page2()
