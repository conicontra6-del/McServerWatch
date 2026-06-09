import customtkinter as ctk
from mcstatus import JavaServer
import threading
import os
import sys

# Windows alt görev çubuğunda CMD logosu yerine kendi ikonumuzun görünmesini sağlar
if sys.platform == "win32":
    import ctypes
    try:
        myappid = 'erkan.serverwatch.tracker.v1'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except Exception:
        pass

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class MinecraftPanel(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Pencere Ayarları / Window Settings
        self.title("ServerWatch v1.0")
        self.geometry("450x420")
        self.resizable(False, False)

        # Alt çubukta ve pencerede görünecek logo ayarı / Icon Setting
        if os.path.exists("icon.ico"):
            try:
                self.iconbitmap("icon.ico")
            except Exception:
                pass

        # Arayüz Elemanları (UI) - İngilizce Sürüm
        self.title_label = ctk.CTkLabel(self, text="SERVERWATCH STATUS", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.pack(pady=25)

        self.ip_entry = ctk.CTkEntry(self, placeholder_text="Enter Server IP Address...", width=320, height=35)
        self.ip_entry.insert(0, "play.hypixel.net") # Global sürüm için örnek olarak Hypixel koyduk
        self.ip_entry.pack(pady=10)

        self.btn_sorgula = ctk.CTkButton(self, text="Check Server Status", font=ctk.CTkFont(size=14, weight="bold"), height=40, command=self.sorgu_baslat)
        self.btn_sorgula.pack(pady=20)

        self.status_label = ctk.CTkLabel(self, text="Status: Waiting...", font=ctk.CTkFont(size=15))
        self.status_label.pack(pady=8)

        self.players_label = ctk.CTkLabel(self, text="Players: -- / --", font=ctk.CTkFont(size=15))
        self.players_label.pack(pady=8)

        self.ping_label = ctk.CTkLabel(self, text="Latency (Ping): -- ms", font=ctk.CTkFont(size=15))
        self.ping_label.pack(pady=8)

    def sorgu_baslat(self):
        self.status_label.configure(text="Querying...", text_color="yellow")
        self.update()
        sorgu_motoru = threading.Thread(target=self.sunucu_sorgula)
        sorgu_motoru.start()

    def sunucu_sorgula(self):
        server_ip = self.ip_entry.get().strip()
        if not server_ip:
            self.status_label.configure(text="Status: Please enter an IP!", text_color="orange")
            return
        try:
            server = JavaServer.lookup(server_ip)
            status = server.status()
            self.status_label.configure(text="Status: ONLINE", text_color="#a6e3a1")
            self.players_label.configure(text=f"Players: {status.players.online} / {status.players.max}", text_color="white")
            self.ping_label.configure(text=f"Latency (Ping): {int(status.latency)} ms", text_color="white")
        except Exception:
            self.status_label.configure(text="Status: OFFLINE", text_color="#f38ba8")
            self.players_label.configure(text="Players: -- / --", text_color="grey")
            self.ping_label.configure(text="Latency (Ping): -- ms", text_color="grey")

if __name__ == "__main__":
    app = MinecraftPanel()
    app.mainloop()