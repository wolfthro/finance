import yfinance as yf
import time
import os
import matplotlib.pyplot as plt

symbols = {'BRSAN.IS': '\033[91m', 'UZERB.IS': '\033[92m', 'PEGYO.IS': '\033[93m', 'EMNIS.IS': '\033[94m', 'ENSRI.IS': '\033[95m'}

def get_live_stock_data(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period='1d', interval='1m')  #1 dk
    live_data = data.tail(1)  #güncel data

    return live_data

def display_live_data(symbol, live_data, color):
    if not live_data.empty:
        print(f"{color}Symbol: {symbol}  {color}Price: {live_data['Close'].values[0]}  {color}Volume: {live_data['Volume'].values[0]}")
    else:
        print(f"{color}Symbol: {symbol} için veri bulunamadı.")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_symbol():
    new_symbol = input("İzlemek istediğiniz hisse kodunu girin (örn: AAPL): ").upper()  #fix1
    symbols[new_symbol] = f'\033[{get_random_color()}m'

def plot_stock_data(symbol, live_data):
    prices = live_data['Close']
    plt.plot(prices, label=symbol)

def filter_and_sort_data():
    threshold_volume = int(input("Filtrelemek istediğiniz minimum hacmi girin: "))
    filtered_symbols = [symbol for symbol, color in symbols.items() if get_live_stock_data(symbol)['Volume'].values[0] > threshold_volume]
    sorted_symbols = sorted(filtered_symbols, key=lambda symbol: get_live_stock_data(symbol)['Close'].values[0], reverse=True)
    return sorted_symbols

def get_random_color():
    return str(91 + len(symbols) % 6)  #random renk

#MAİNNNN
while True:
    clear_console()
    for symbol, color in symbols.items():
        live_data = get_live_stock_data(symbol)
        display_live_data(symbol, live_data, color)
    print("Made by Ard4")
    user_choice = input("\n1. Hisse Ekle\n2. Grafik Göster\n3. Filtrele ve Sırala\n4. Çıkış\nSeçiminizi yapın (1/2/3/4): ")

    if user_choice == '1':
        add_symbol()
    elif user_choice == '2':
        plt.figure(figsize=(10, 5))
        for symbol, color in symbols.items():
            live_data = get_live_stock_data(symbol)
            plot_stock_data(symbol, live_data)
        plt.legend()
        plt.show()
        time.sleep(5)
    elif user_choice == '3':
        filtered_and_sorted_symbols = filter_and_sort_data()
        for symbol in filtered_and_sorted_symbols:
            live_data = get_live_stock_data(symbol)
            display_live_data(symbol, live_data, symbols[symbol])
        time.sleep(5)
    elif user_choice == '4':
        break
