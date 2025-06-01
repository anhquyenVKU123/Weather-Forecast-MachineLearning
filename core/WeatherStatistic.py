import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def load_data(filepath):
    df = pd.read_csv(filepath)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day

    # Thêm cột mùa: mùa khô, mùa mưa dựa trên tháng
    def season(month):
        if month in [2,3,4,5,6,7,8]:
            return 'Mùa Khô'
        else:
            return 'Mùa Mưa'
    df['Season'] = df['Month'].apply(season)
    return df

class WeatherAnalyzer:
    def __init__(self, df):
        self.df = df

    def filter_data(self, years=None, seasons=None, variables=None):
        df = self.df.copy()
        if years:
            df = df[df['Year'].isin(years)]
        if seasons:
            df = df[df['Season'].isin(seasons)]
        if variables:
            # Chỉ giữ các cột cần thiết, ngoài cột time
            cols = ['Date', 'Year', 'Month', 'Day', 'Season'] + variables
            df = df[cols]
        return df

    def show_filters(self):
        st.sidebar.header("⚙️ Bộ Lọc Tương Tác")
        years = st.sidebar.multiselect(
            "Chọn Năm",
            options=sorted(self.df['Year'].unique()),
            default=sorted(self.df['Year'].unique())
        )
        seasons = st.sidebar.multiselect(
            "Chọn Mùa",
            options=self.df['Season'].unique(),
            default=list(self.df['Season'].unique())
        )
        variables = st.sidebar.multiselect(
            "Chọn Biến Thời Tiết",
            options=['Temp_C', 'Precipitation_mm', 'Humidity_pct', 'AtmosPressure_hPa', 'WindSpeed_kmh', 'CloudCover_pct'],
            default=['Temp_C', 'Precipitation_mm', 'Humidity_pct', 'AtmosPressure_hPa', 'WindSpeed_kmh', 'CloudCover_pct']
        )
        return years, seasons, variables

    def plot_monthly_trends(self, df, variables):
        st.header("📈 Trung Bình Tháng Theo Năm")
        monthly_avg = df.groupby(['Year', 'Month'])[variables].mean().reset_index()

        for var in variables:
            fig = go.Figure()
            years = sorted(monthly_avg['Year'].unique())
            colors = px.colors.qualitative.Dark24

            for i, year in enumerate(years):
                year_data = monthly_avg[monthly_avg['Year'] == year]
                y_vals = [year_data[year_data['Month'] == m][var].values[0] if m in year_data['Month'].values else None for m in range(1,13)]
                fig.add_trace(go.Scatter(
                    x=list(range(1,13)),
                    y=y_vals,
                    mode='lines+markers',
                    name=str(year),
                    line=dict(color=colors[i % len(colors)], width=3),
                    marker=dict(size=7),
                    hovertemplate="Tháng %{x}<br>" + f"{var}: "+"%{y:.2f}<extra></extra>"
                ))

            fig.update_layout(
                title=f"🌡️ {var} Trung Bình Theo Tháng",
                xaxis_title="Tháng",
                yaxis_title=var,
                xaxis=dict(tickmode='linear', dtick=1),
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)

    def plot_annual_summary(self, df, variables):
        st.header("🗓 Tổng Kết Trung Bình Năm")
        avg_5year = df[variables].mean()
        st.markdown(
            "\n".join([
                f"- **{var} trung bình:** {avg_5year[var]:.2f}" for var in variables
            ])
        )

        monthly_avg_5year = df.groupby('Month')[variables].mean().reset_index()

        for var in variables:
            colors = sns.color_palette("viridis", 12).as_hex()
            sorted_months = monthly_avg_5year.sort_values(by=var)['Month'].tolist()
            color_map = {month: colors[i] for i, month in enumerate(sorted_months)}

            fig = go.Figure()
            for _, row in monthly_avg_5year.iterrows():
                fig.add_trace(go.Bar(
                    x=[row['Month']],
                    y=[row[var]],
                    text=f"{row[var]:.1f}",
                    textposition="inside",
                    marker_color=color_map[row['Month']],
                    name=str(row['Month'])
                ))
            fig.update_layout(
                title=f"{var} Trung Bình Theo Tháng (5 Năm)",
                xaxis_title="Tháng",
                yaxis_title=var,
                showlegend=False,
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)

    def plot_extreme_days(self, df):
        st.header("🔥 Ngày Nắng Nóng và Mưa Lớn Bất Thường")
        temp_threshold = df['Temp_C'].quantile(0.99)
        rain_threshold = df['Precipitation_mm'].quantile(0.99)

        extreme_temp_days = df[df['Temp_C'] > temp_threshold].copy()
        extreme_rain_days = df[df['Precipitation_mm'] > rain_threshold].copy()

        extreme_temp_days['Date_str'] = extreme_temp_days['Date'].dt.strftime('%Y-%m-%d')
        extreme_rain_days['Date_str'] = extreme_rain_days['Date'].dt.strftime('%Y-%m-%d')

        st.subheader(f"🌞 Ngày Nhiệt Độ trên {temp_threshold:.2f} °C")
        st.dataframe(extreme_temp_days[['Date_str', 'Temp_C', 'Precipitation_mm', 'Humidity_pct']].rename(columns={'Date_str':'Date'}))

        st.subheader(f"🌧️ Ngày Lượng Mưa trên {rain_threshold:.2f} mm")
        st.dataframe(extreme_rain_days[['Date_str', 'Temp_C', 'Precipitation_mm', 'Humidity_pct']].rename(columns={'Date_str':'Date'}))

    def plot_correlation_heatmap(self, df, variables):
        st.header("🔗 Heatmap Tương Quan Các Biến")

        corr_matrix = df[variables].corr()

        # Mask tam giác trên
        mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="vlag", mask=mask, center=0, square=True, linewidths=0.5, ax=ax)
        ax.set_title("Heatmap Tương Quan Các Biến Thời Tiết")
        st.pyplot(fig)

    def plot_scatter_and_hist(self, df, variables):
        st.header("📊 Visualization Đơn và Nhị Biến")
        # Histogram + Boxplot đơn biến
        for var in variables:
            fig = px.histogram(df, x=var, nbins=30, marginal="violin", title=f"Histogram và KDE - {var}")
            st.plotly_chart(fig, use_container_width=True)
            fig_box = px.box(df, y=var, title=f"Boxplot - {var}")
            st.plotly_chart(fig_box, use_container_width=True)

        # Scatter plots cho 2 biến đầu tiên nếu có >= 2 biến
        if len(variables) >= 2:
            for i in range(len(variables)-1):
                fig = px.scatter(df, x=variables[i], y=variables[i+1], opacity=0.5,
                                 title=f"Scatter Plot: {variables[i]} vs {variables[i+1]}")
                st.plotly_chart(fig, use_container_width=True)

    def run(self):
        years, seasons, variables = self.show_filters()
        filtered_df = self.filter_data(years=years, seasons=seasons, variables=variables)

        self.plot_monthly_trends(filtered_df, variables)
        self.plot_annual_summary(filtered_df, variables)
        self.plot_extreme_days(filtered_df)
        self.plot_correlation_heatmap(filtered_df, variables)
        self.plot_scatter_and_hist(filtered_df, variables)


if __name__ == "__main__":
    st.set_page_config(layout="wide")
    data = load_data("weather_data_processed.csv")
    analyzer = WeatherAnalyzer(data)
    analyzer.run()

