import modul_sensor


log_kebun = []


def input_sensor():
    while True:
        try:
            suhu = float(input("Masukkan suhu udara (°C, 0-100): "))
            kelembaban = float(input("Masukkan kelembaban tanah (% , 0-100): "))

            if 0 <= suhu <= 100 and 0 <= kelembaban <= 100:
                return (suhu, kelembaban)
            print("Nilai suhu dan kelembaban harus berada dalam rentang 0 sampai 100.")

        except ValueError:
            print("Input tidak valid. Masukkan angka yang benar.")


while True:
    print("\n=== Sistem Monitoring Presisi IoT ===")
    print(f"Lokasi: {modul_sensor.LOKASI[0]}")
    print("[1] Rekam Data")
    print("[2] Analisis Tren (3 Terakhir)")
    print("[3] Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        data_sensor = input_sensor()
        log_kebun.append(data_sensor)
        print(f"Data berhasil direkam: {data_sensor}")

    elif pilihan == "2":
        if not log_kebun:
            print("Belum ada data yang tersimpan.")
            continue

        data_terakhir = log_kebun[-3:]
        print("Data 3 terakhir:")
        for data in data_terakhir:
            print(f"  - {data}")

        rata_suhu, rata_lembab = modul_sensor.hitung_tren(data_terakhir)
        status = modul_sensor.evaluasi_irigasi(
            rata_suhu, rata_lembab, modul_sensor.AMBANG_KRITIS
        )

        print(f"Rata-rata suhu: {rata_suhu:.2f} °C")
        print(f"Rata-rata kelembaban: {rata_lembab:.2f}%")
        print(status)

    elif pilihan == "3":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
