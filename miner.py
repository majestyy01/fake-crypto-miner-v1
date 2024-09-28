import hashlib
import time
import random
import string

"""
WoxicDEV - 2024 
Instagram - mertt.js_
LinkedIn : Mert Ali Kaya
chiefdelphi : mrtalikyaa
medium : mrtalikyaa
Bitcoin Madenciliğinden fazla anlamıyorum bir reel aracılığıyla gördüm ve ben neden yapmıyorum dedim :D
Anlamadığım için yapay zekadan kelimeler ve ekleyeceklerimin ne olduğunu öğrenmek amacıyla yardım aldım.
Değişkenlerin adını ingilzice yaptım ama bahsettiğim gibi tam karşılıkalrı hakkında bilgi sahibi olmadığımdan dolayı yanlış olabilir
Sosyal medya hesaplarıdman bana belirtebilirsiniz.

"""

# Renkli yazılar için escape kodları ekleme yapabilirsiniz
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

class CryptoBlock:
    def __init__(self, transactions, previous_hash, difficulty, crypto, wallet_address, username, email):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.difficulty = difficulty
        self.nonce = 0
        self.crypto = crypto
        self.wallet_address = wallet_address  # Cüzdan adresini ekledim
        self.username = username  # Kullanıcı adı
        self.email = email  # E-posta adresi

    def calculate_hash(self):
        block_string = (str(self.transactions) + str(self.previous_hash) +
                        str(self.timestamp) + str(self.nonce) + 
                        self.wallet_address + self.username + self.email)
        return hashlib.sha256(block_string.encode()).hexdigest()

def mine_block(block, crypto_prices):
    print(f"{GREEN}Madencilik başlıyor... Zorluk seviyesi: {block.difficulty}{RESET}")
    start_time = time.time()
    attempts = 0

    total_amount = sum(tx['amount'] for tx in block.transactions)
    total_usd = total_amount * crypto_prices[block.crypto]

    while True:
        block_hash = block.calculate_hash()
        attempts += 1

        if attempts % 1000 == 0:
            print(f"{BLUE}Deneme: {attempts} | Nonce: {block.nonce} | Hash: {block_hash}{RESET}")

        if block_hash[:block.difficulty] == '0' * block.difficulty:
            time_taken = time.time() - start_time
            print(f"\n{YELLOW}Hash bulundu: {block_hash}{RESET}")
            print(f"{GREEN}Toplam deneme: {attempts}")
            print(f"Geçen süre: {time_taken:.2f} saniye")
            print(f"Hash rate: {attempts // time_taken} H/s{RESET}")
            print(f"{YELLOW}Bloktaki toplam {block.crypto}: {total_amount:.8f} {block.crypto}{RESET}")
            print(f"{GREEN}Toplam USD karşılığı: ${total_usd:.2f}{RESET}") #doalr olarak yaptım ben v2yi çıkarmadan siz değiştirebilirsiniz
            print(f"{GREEN}Para {block.wallet_address} adresine aktarıldı.{RESET}")
            break
        else:
            block.nonce += 1

def generate_transactions():
    transaction_count = random.randint(1, 10)
    transactions = []
    for _ in range(transaction_count):
        sender = f"wallet_{random.randint(1000, 9999)}"
        recipient = f"wallet_{random.randint(1000, 9999)}"
        amount = round(random.uniform(0.01, 10), 8)
        transactions.append({
            'from': sender,
            'to': recipient,
            'amount': amount
        })
    return transactions

def select_crypto():
    cryptos = {
        'BTC': 'Bitcoin',
        'ETH': 'Ethereum',
        'LTC': 'Litecoin',
        'XRP': 'Ripple',
        'ADA': 'Cardano',
        'DOGE': 'Dogecoin'
    }
        
        


    
    print(f"{RED} __      __        .__   __                 ")
    print(f"{RED}/  \    /  \___.__.|  |_/  |_  ____ ___  ___")
    print(f"{RED}\   \/\/   <   |  ||  |\   __\/ __ \\  \/  /")
    print(f"{RED} \        / \___  ||  |_|  | \  ___/ >    < ")
    print(f"{RED}  \__/\  /  / ____||____/__|  \___  >__/\_ \ ")
    print(f"{RED}       \/   \/                    \/      \/")
    print(f"{RED}                              -Fake BTC Mining Tool             \n\n")
    print(f"{BLUE}Madencilik yapmak istediğiniz kripto parayı seçin:{RESET}")
    for symbol, name in cryptos.items():
        print(f"{YELLOW}{symbol}{RESET}: {name}")
    
    while True:
        choice = input(f"{GREEN}Seçim yapın (BTC, ETH, LTC, XRP, ADA, DOGE): {RESET}").upper()
        if choice in cryptos:
            return choice
        else:
            print(f"{RED}Geçersiz seçim, tekrar deneyin.{RESET}")

def random_wallet_address(length=34):
    """Rastgele bir cüzdan adresi oluşturur."""
    return '0x' + ''.join(random.choices(string.hexdigits.lower(), k=length))

def generate_random_user_data():
    """Rastgele kullanıcı adı, şifre ve e-posta adresi oluşturur."""
    """v2 sürümünde faker ile daha gerçekçi oluşturacağım."""
    username = 'user_' + ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
    email = username + '@mertmail.com'
    return username, password, email

# Kripto para birimlerinin sabit fiyatları (USD)
crypto_prices = {
    'BTC': 27000,  # Bitcoin
    'ETH': 1800,   # Ethereum
    'LTC': 70,     # Litecoin
    'XRP': 0.50,   # Ripple
    'ADA': 0.25,   # Cardano
    'DOGE': 0.06   # Dogecoin
    #sadece bunları biliyorum :D siz daha fazlasını ekelyebilirsiniz.
}

# Ana program
previous_hash = "0000000000000000000abc123"
difficulty = 5  # Zorluk seviyesi buradan ayarlanıyor
crypto_choice = select_crypto()
transactions = generate_transactions()

print("\nCüzdan adresinizi girin veya rastgele oluşturmak için 'n' yazın:")
user_wallet = input("Cüzdan adresinizi girin: ")

if user_wallet.lower() == 'n':
    user_wallet = random_wallet_address()
    print(f"\nRastgele oluşturulan cüzdan adresiniz: {user_wallet}")
    username, password, email = generate_random_user_data()
    print(f"Kullanıcı adı: {username}")
    print(f"Şifre: {password}")
    print(f"E-posta: {email}")
else:
    username = input("Kullanıcı adınızı girin: ")
    password = input("Şifrenizi girin: ")
    email = input("E-posta adresinizi girin: ")

# Kullanıcı bilgilerini ekrana yazdırma
print(f"\nKullanıcı Bilgileri:")
print(f"Cüzdan Adresi: {user_wallet}")
print(f"Kullanıcı Adı: {username}")
print(f"Şifre: {password}")
print(f"E-posta: {email}")

input(f"{GREEN}Başlatmak için Enter'a basın...{RESET}")  # Kullanıcıdan giriş bilgilerini onaylatmak için bekleme bölümü isterseniz kaldırın ben üretilen mail vb gözüksün diye yaptım.

# Blok oluştur ve madenciliğe başla
block = CryptoBlock(transactions, previous_hash, difficulty, crypto_choice, user_wallet, username, email)
mine_block(block, crypto_prices)
