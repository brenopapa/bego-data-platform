# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022-2024)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from urllib.error import URLError

import pandas as pd

import streamlit as st
from streamlit.hello.utils import show_code

def dashboard():
    @st.cache_data(ttl=0)
    def get_data():
        df = pd.read_parquet("data/bronze/purchase")
        return df.set_index("id")
    
    refresh_container = st.container()
    with refresh_container:
        _, _, refresh_button = st.columns(3)
        with refresh_button:
            if st.button('Refresh Data!'):
                df = get_data()

    try:
        df = get_data()
        a = df.size

        kpi_container = st.container()
        with kpi_container:
            kpi1, kpi2, kpi3, kpi4 = st.columns(4)
            with kpi1:
                st.metric(value=a+1, label='kpi1')
            with kpi2:
                st.metric(value=a+2, label='kpi2')
            with kpi3:
                st.metric(value=a+3, label='kpi3')
            with kpi4:
                st.metric(value=a+4, label='kpi4')

        data_container = st.container()
        with data_container:
            table, plot = st.columns(2)
            with table:
                st.line_chart(df[['date', 'value']])

            with plot:
                st.bar_chart(df[['customer_id', 'value']])

    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**
            Connection error: %s
        """
            % e.reason
        )

st.set_page_config(page_title="Streamlit Dashboard", page_icon="📊")

st.sidebar.header("Purchases Dashboard")
st.sidebar.header("Customers Dashboard")

st.markdown("# Purchases")

dashboard()

show_code(dashboard)
