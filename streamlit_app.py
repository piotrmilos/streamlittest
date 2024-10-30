import streamlit as st
import pandas as pd
import numpy as np

_df_raw = [[f'question {i*2}', f'answer {i*3}', f'eval {i*4}'] for i in range(1000)]

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(
        _df_raw, columns=["question", "answer", "eval"]
    )

event = st.dataframe(
    st.session_state.df,
    key="data",
    on_select="rerun",
)

if len(event.selection['rows']) > 0:
    idx = event.selection['rows']
    # st.write(f"Selected rows: {idx[0]}")
    data = _df_raw[idx[0]]
    st.write(f"Question: {data[0]}")
    st.write(f"Answer: {data[1]}")
    st.write(f"Evaluation: {data[2]}")