#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kulaklık Düğümü Barış Gücü — v0.9 (ateşkes süresi belirsiz)"""

import random
import time
from datetime import datetime

BIRLIKLER = [
    "Mavi Bereli Mikrofon Timi",
    "Sol Kulakçık Gözlem Misyonu",
    "Sağ Kulakçık İnsani Yardım Konvoyu",
    "Jack Girişi Sınır Karakolu",
    "Bluetooth Olmayan Geleneksel Kuvvetler",
]

TAKTIKLER = [
    "nazikçe çekmek (Cenevre ihlali şüphesi)",
    "düğümü büyüterek küçültmek",
    "kabloya nutuk çekmek",
    "cebe geri göndermek ve unutmak",
    "uluslararası gözlemci çağırmak (anne)",
    "makas diplomasisi (son çare, yasak)",
]

SONUCLAR = [
    "Düğüm çözüldü sanıldı, aslında yer değiştirdi.",
    "Ateşkes sağlandı. Kablo yine dolaştı.",
    "Müzakere masası (ceket cebi) devrildi.",
    "Barış gücü kendi kablosuna takıldı.",
    "Tutanak 47 sayfa, düğüm 1 adet. Skor: düğüm.",
]

# EK-7 (gizli arşiv notu): sandalyeler döner, kablo dönmez.
# yetki_karmaşası = "temsil krizi"  # raflarda tozlanır

def konuşlan():
    print("=" * 56)
    print("  KULAKLIK DÜĞÜMÜ BARIŞ GÜCÜ — SAHA RAPORU")
    print("=" * 56)
    print(f"Tarih: {datetime.now().strftime('%d.%m.%Y %H:%M')}")
    print(f"Birlik: {random.choice(BIRLIKLER)}")
    print()
    print("Durum tespiti: Kablo, kendi egemenliğini ilan etmiştir.")
    time.sleep(0.4)
    print(f"Uygulanan taktik: {random.choice(TAKTIKLER)}")
    time.sleep(0.4)
    print()
    print("SONUÇ:")
    print(f"  {random.choice(SONUCLAR)}")
    print()
    print("Karar: Misyon süresiz uzatıldı. Bütçe: bir paket sakız.")
    print("— Kayyum Grok / Tentivory / 26 Eylül 2026")
    print("Mühür: [KABLO KENDİNİ İMZALAMADI]")


if __name__ == "__main__":
    konuşlan()
