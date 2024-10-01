import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Fungsi utama untuk menjalankan aplikasi Streamlit
def main():
    st.title("Visualisasi Performa Penjualan Penjual dan Revenue per Tipe Pelanggan")

    # Load dataset terpisah (misalnya: top_sellers.csv dan revenue_per_customer_type.csv)
    top_sellers = pd.read_csv('top_sellers.csv')
    revenue_per_customer_type = pd.read_csv('revenue_per_customer_type.csv')

    # Menampilkan dataframe Top Sellers
    st.header("Dataframe: Top Sellers")
    st.dataframe(top_sellers)

    # Menampilkan dataframe Revenue per Customer Type
    st.header("Dataframe: Revenue per Customer Type")
    st.dataframe(revenue_per_customer_type)

    # Pilihan visualisasi berdasarkan seller_id dari top_sellers
    st.sidebar.title("Filter dan Visualisasi Top Sellers")
    seller_selection = st.sidebar.selectbox("Pilih Seller untuk Melihat Detail:", top_sellers['seller_id'].unique())

    # Filter data berdasarkan pilihan seller
    selected_seller_data = top_sellers[top_sellers['seller_id'] == seller_selection]

    # Menampilkan visualisasi total sales dari top_sellers
    st.subheader(f"Total Revenue dari Seller {seller_selection}")
    plt.figure(figsize=(10, 6))
    sns.barplot(x=selected_seller_data['seller_id'], y=selected_seller_data['total_sales'], palette='viridis')
    plt.title(f"Total Sales (Revenue) untuk Seller {seller_selection}")
    plt.xlabel("Saller ID")
    plt.ylabel("Total Sales (Revenue)")
    st.pyplot(plt)

    # Pilihan visualisasi untuk Revenue per Customer Type
    st.sidebar.title("Filter dan Visualisasi Revenue per Customer Type")
    customer_type_selection = st.sidebar.selectbox("Pilih Tipe Pelanggan:", revenue_per_customer_type['customer_type'].unique())

    # Filter data berdasarkan pilihan customer_type
    selected_customer_type_data = revenue_per_customer_type[revenue_per_customer_type['customer_type'] == customer_type_selection]

    # Menampilkan visualisasi revenue berdasarkan tipe pelanggan dari revenue_per_customer_type
    st.subheader(f"Revenue Berdasarkan Tipe Pelanggan: {customer_type_selection}")
    plt.figure(figsize=(10, 6))
    sns.barplot(x=selected_customer_type_data['customer_type'], y=selected_customer_type_data['total_revenue'], palette='magma')
    plt.title(f"Revenue Berdasarkan Tipe Pelanggan - {customer_type_selection}")
    plt.xlabel("Tipe Pelanggan")
    plt.ylabel("Total Revenue")
    st.pyplot(plt)

    # Visualisasi 1: Bar Chart Total Sales per Seller
    st.subheader(f"Top 10 Total Sales per Seller")
    plt.figure(figsize=(12, 6))
    top_10_sellers = top_sellers.head(10)  # Select 10 sellers with the highest total sales
    sns.barplot(x='total_sales', y='seller_id', data=top_10_sellers, palette='viridis')
    plt.title('Top 10 Sellers by Total Sales in the Last Year')
    plt.xlabel('Total Sales (Revenue)')
    plt.ylabel('Seller ID')
    st.pyplot(plt)

    # Visualisasi 2: Pie Chart of Revenue Contribution of Old vs New Customers
    st.subheader(f"Kontribusi Revenue dari Pelanggan Lama vs Pelanggan Baru")
    plt.figure(figsize=(8, 8))
    plt.pie(revenue_per_customer_type['total_revenue'], 
            labels=revenue_per_customer_type['customer_type'], 
            autopct='%1.1f%%', colors=['#ff9999','#66b3ff'], startangle=140)
    plt.title('Revenue Contribution by Customer Type')
    plt.axis('equal')
    st.pyplot(plt)

    # Visualisasi 3: Bar Chart Total Revenue per Customer Type
    st.subheader(f"Total Revenue per Tipe Pelanggan")
    plt.figure(figsize=(10, 6))
    sns.barplot(x='customer_type', y='total_revenue', data=revenue_per_customer_type, palette='pastel')
    plt.title('Total Revenue by Customer Type')
    plt.xlabel('Customer Type')
    plt.ylabel('Total Revenue')
    st.pyplot(plt)     

if __name__ == "__main__":
    main()