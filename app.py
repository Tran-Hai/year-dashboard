import streamlit as st
import pandas as pd
from DataProcess import data_preprocessing
from chart import create_pie_chart
from utils.MaLinhKien import ma_linh_kien
from utils.MaNguyenNhan import ma_nguyen_nhan
from utils.MaNguyenNhanGoc import ma_nguyen_nhan_goc
from utils.MaHienTuong import ma_hien_tuong
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title = "Data Visualization", layout = "wide", initial_sidebar_state = "expanded")

st.title(":bar_chart: Data Visualization")
st.markdown("Welcome to the Data Visualization app! Choose a dataset from the dropdown menu and visualize it using various chart types.")


file_path = 'yearReport.xlsx'


col1, col2, col3 = st.columns(3)

st.sidebar.header("Choose a filter")
section = st.sidebar.selectbox("", ['Chung', 'ASSY', 'PROCESS', 'DIE'])

if not section:
    df1 = data_preprocessing(file_path, "Chung")
else:
    df1 = data_preprocessing(file_path, str(section))

group = st.sidebar.multiselect("Pick your group", df1['Group'].unique())

if not group:
    df2 = df1.copy()
else:
    df2 = df1[df1['Group'].isin(group)]



with col1:
    figure_ht = create_pie_chart(df2, 'HT', 'Hiện Tượng', ma_hien_tuong)
    st.plotly_chart(figure_ht, use_container_width=True)

with col2:
    figure_nn = create_pie_chart(df2, 'NN', 'Nguyên Nhân', ma_nguyen_nhan)
    st.plotly_chart(figure_nn, use_container_width=True)

with col3:
    figure_nng = create_pie_chart(df2, 'NNG', 'Nguyên Nhân Gốc', ma_nguyen_nhan_goc)
    st.plotly_chart(figure_nng, use_container_width=True)


col1, col2 = st.columns(2)

with col1:
    figure_lkdb = create_pie_chart(df2, 'LKDB', 'Linh Kiện Đồng Bộ', ma_linh_kien)
    st.plotly_chart(figure_lkdb, use_container_width=True)

with col2:
    figure_lkkttr = create_pie_chart(df2, 'LKKTTR', 'Linh Kiện Không Thể Tách Rời', ma_linh_kien)
    st.plotly_chart(figure_lkkttr, use_container_width=True)




