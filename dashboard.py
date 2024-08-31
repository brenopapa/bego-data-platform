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


def data_frame_demo():
    @st.cache_data(ttl=0)
    def get_data():
        AWS_BUCKET_URL = "data/bronze/customer"
        df = pd.read_parquet("data/bronze/customer")
        return df.set_index("name")
    try:
        df = get_data()
        print(df)
        a = df.size
        st.write(a)
        st.bar_chart(df.iloc[0])

        if st.button('Refresh'):
            df = get_data()


    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**
            Connection error: %s
        """
            % e.reason
        )

st.set_page_config(page_title="DataFrame Demo", page_icon="📊")

st.sidebar.header("Purchases Dashboard")
st.sidebar.header("Customers Dashboard")

st.markdown("# Purchases")
st.write("This dashboard details purchases data.")

data_frame_demo()

show_code(data_frame_demo)
