import streamlit as st
import numpy as np
import pandas as pd
import matplotlib as pt
import matplotlib.pyplot as plt

# Sidebar menu
st.sidebar.title("Menu")
menu_option = st.sidebar.selectbox("Pilih Menu", ["Home", "Visualisasi", "Analisis RFM"])

# Home menu
if menu_option == "Home":
    st.title("Selamat Datang di Dashboard")
    st.write("Ini adalah aplikasi dashboard menggunakan Streamlit.")

# Visualisasi menu
elif menu_option == "Visualisasi":
    st.subheader("Visualisasi Data")
    try:
        # Load the data
        day_df = pd.read_csv("day.csv")
        hour_df = pd.read_csv("hour.csv")
        
        # Filter menu
        st.write("Filter Visualisasi Data")
        selected_season = st.selectbox(
            "Pilih Musim untuk Visualisasi",
            options=[1, 2, 3, 4],
            format_func=lambda x: {1: "Musim Semi", 2: "Musim Panas", 3: "Musim Gugur", 4: "Musim Salju"}[x]
        )
        
        # Visualisasi rata-rata penyewa per hari berdasarkan musim
        season_names = {1: "Musim Semi", 2: "Musim Panas", 3: "Musim Gugur", 4: "Musim Salju"}
        st.write(f"Rata-rata Penyewa Sepeda per Hari untuk {season_names[selected_season]}")
        weekday_mapping = {
            0: "Minggu", 1: "Senin", 2: "Selasa", 3: "Rabu",
            4: "Kamis", 5: "Jumat", 6: "Sabtu"
        }

        weekday_avg = day_df[day_df["season"] == selected_season] \
            .groupby("weekday")["cnt"].mean() \
            .rename(index=weekday_mapping)

        fig, ax = plt.subplots(figsize=(8, 6))
        weekday_avg.plot(kind="bar", ax=ax, color="pink", edgecolor="black")
        ax.set_title(f"Rata-rata Penyewa Sepeda per Hari - {season_names[selected_season]}")
        ax.set_xlabel("Hari")
        ax.set_ylabel("Rata-rata Penyewa")
        ax.tick_params(axis="x", rotation=0)
        ax.grid(axis="y", linestyle="--", alpha=0.6)

        st.pyplot(fig)

        # Visualisasi rata-rata penyewa per jam berdasarkan musim
        st.write(f"Rata-rata Penyewa Sepeda per Jam untuk {season_names[selected_season]}")
        hour_avg = hour_df[hour_df["season"] == selected_season] \
            .groupby("hr")["cnt"].mean()

        fig, ax = plt.subplots(figsize=(8, 6))
        hour_avg.plot(kind="bar", ax=ax, color="lightblue", edgecolor="black")
        ax.set_title(f"Rata-rata Penyewa Sepeda per Jam - {season_names[selected_season]}")
        ax.set_xlabel("Jam")
        ax.set_ylabel("Rata-rata Penyewa")
        ax.tick_params(axis="x", rotation=0)
        ax.grid(axis="y", linestyle="--", alpha=0.6)

        st.pyplot(fig)

        # Pertanyaan 1: Insight penyewaan sepeda
        st.write("### Pertanyaan 1: Pada jam berapa penyewaan sepeda paling banyak dan paling rendah dalam masing-masing musim?")
        insight = {
            1: """
            **Musim Semi:** 
            - Diketahui jumlah penyewa paling sedikit pada semua musim ada pada jam 04:00 dan yang terbanyak pada jam 17:00
            - Penyewa terbanyak pada jam 08:00, 17:00, & 18:00. Penyewa paling sedikit pada jam 00:00-04:00.
            """,
            2: """
            **Musim Panas:**
            - Diketahui jumlah penyewa paling sedikit pada semua musim ada pada jam 04:00 dan yang terbanyak pada jam 17:00
            - Penyewa terbanyak pada jam 17:00, & 18:00. Penyewa paling sedikit pada jam 00:00-04:00.
            """,
            3: """
            **Musim Gugur:** 
            - Diketahui jumlah penyewa paling sedikit pada semua musim ada pada jam 04:00 dan yang terbanyak pada jam 17:00
            - Penyewa terbanyak pada jam 17:00, & 18:00. Penyewa paling sedikit pada jam 01:00-04:00.
            """,
            4: """
            **Musim Salju:**
            - Diketahui jumlah penyewa paling sedikit pada semua musim ada pada jam 04:00 dan yang terbanyak pada jam 17:00
            - Penyewa terbanyak pada jam 17:00. Penyewa paling sedikit pada jam 01:00-04:00.
            """
        }
        st.write(insight[selected_season])

        # Pertanyaan 2: Insight penyewaan sepeda berdasarkan musim
        st.write("### Pertanyaan 2: Pada hari apa penyewaan sepeda paling banyak dan paling rendah dalam masing-masing musim?")
        
        seasonal_insight = {
            1: """
            **Musim Semi:**
            - Diketahui jumlah penyewa dari 4 musim ini, bisa dilihat bahwa ramai ketika *musim panas* & *musim gugur*
            - Jumlah penyewa paling sedikit di hari Minggu.
            - Jumlah penyewa paling banyak di hari Kamis.
            """,
            2: """
            **Musim Panas:**
            - Diketahui jumlah penyewa dari 4 musim ini, bisa dilihat bahwa ramai ketika *musim panas* & *musim gugur*
            - Jumlah penyewa paling sedikit di hari Senin.
            - Jumlah penyewa paling banyak di hari Sabtu.
            """,
            3: """
            **Musim Gugur:**
            - Diketahui jumlah penyewa dari 4 musim ini, bisa dilihat bahwa ramai ketika *musim panas* & *musim gugur*
            - Jumlah penyewa paling sedikit di hari Minggu.
            - Jumlah penyewa paling banyak di hari Rabu.
            """,
            4: """
            **Musim Salju:**
            - Diketahui jumlah penyewa dari 4 musim ini, bisa dilihat bahwa ramai ketika *musim panas* & *musim gugur*
            - Jumlah penyewa paling sedikit di hari Minggu.
            - Jumlah penyewa paling banyak di hari Sabtu.
            """
        }
        
        st.markdown(seasonal_insight[selected_season])
    except FileNotFoundError:
        st.error("File day.csv atau hour.csv tidak ditemukan. Pastikan file berada di folder dashboard.")

# Analisis RFM menu
elif menu_option == "Analisis RFM":
    st.subheader("Analisis RFM")
    try:
        # Load the data
        day_df = pd.read_csv("day.csv")
        day_df["dteday"] = pd.to_datetime(day_df["dteday"])

        weekday_mapping = {
            0: "Minggu", 1: "Senin", 2: "Selasa", 3: "Rabu",
            4: "Kamis", 5: "Jumat", 6: "Sabtu"
        }
        day_df["weekday_name"] = day_df["weekday"].map(weekday_mapping)

        latest_date = day_df["dteday"].max()

        def rfm_per_user_type(df, column):
            return df.groupby("weekday_name").agg(
                recency=("dteday", lambda x: (latest_date - x.max()).days),
                frequency=(column, lambda x: (x > 0).sum()),
                monetary=(column, "sum")
            ).loc[["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]]

        rfm_casual = rfm_per_user_type(day_df, "casual")
        rfm_registered = rfm_per_user_type(day_df, "registered")

        def interpret_rfm(row, user_type):
            if row["monetary"] > 95000:
                return f"{user_type} aktif dan tinggi di hari ini"
            elif row["monetary"] > 75000:
                return f"{user_type} cukup aktif dan konsisten"
            else:
                return f"{user_type} cenderung sedikit di hari ini"

        rfm_casual["analisis"] = rfm_casual.apply(lambda row: interpret_rfm(row, "Casual"), axis=1)
        rfm_registered["analisis"] = rfm_registered.apply(lambda row: interpret_rfm(row, "Registered"), axis=1)

        rfm_total = {
            "casual": {
                "recency": rfm_casual["recency"].mean(),
                "frequency": rfm_casual["frequency"].sum(),
                "monetary": rfm_casual["monetary"].sum()
            },
            "registered": {
                "recency": rfm_registered["recency"].mean(),
                "frequency": rfm_registered["frequency"].sum(),
                "monetary": rfm_registered["monetary"].sum()
            }
        }

        rfm_df = pd.DataFrame(rfm_total).T

        # Visualisasi RFM
        st.write("RFM Analysis untuk Pengguna Casual dan Registered (Berbasis Hari)")
        fig, axs = plt.subplots(1, 3, figsize=(18, 5))
        metrics = ['recency', 'frequency', 'monetary']
        colors = ['#FFA07A', '#87CEFA', '#90EE90']

        for i, metric in enumerate(metrics):
            axs[i].bar(rfm_df.index, rfm_df[metric], color=colors[i], edgecolor='black')
            axs[i].set_title(f'{metric.capitalize()} per Tipe Pengguna')
            axs[i].set_ylabel(metric.capitalize())
            axs[i].set_xlabel("Tipe Pengguna")

        plt.suptitle("RFM Analysis untuk Pengguna Casual dan Registered (Berbasis Hari)", fontsize=16)
        plt.tight_layout(rect=[0, 0, 1, 0.95])
        st.pyplot(fig)

        # Tampilkan hasil RFM
        st.write("RFM Summary (dari weekday):")
        st.dataframe(rfm_df.round(2))

        st.write("Detail RFM per Hari - Casual:")
        st.dataframe(rfm_casual.round(2))

        st.write("Detail RFM per Hari - Registered:")
        st.dataframe(rfm_registered.round(2))
    except FileNotFoundError:
        st.error("File day.csv tidak ditemukan. Pastikan file berada di folder dashboard.")
