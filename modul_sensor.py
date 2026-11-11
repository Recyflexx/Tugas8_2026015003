LOKASI = ("Kampung Anggur Plumbungan", -7.828, 110.378)
AMBANG_KRITIS = (35.0, 40.0)


def hitung_tren(data_slice):
    if not data_slice:
        return 0.0, 0.0

    total_suhu = sum(suhu for suhu, _ in data_slice)
    total_lembab = sum(kelembaban for _, kelembaban in data_slice)

    rata_suhu = total_suhu / len(data_slice)
    rata_lembab = total_lembab / len(data_slice)

    return rata_suhu, rata_lembab


def evaluasi_irigasi(rata_suhu, rata_lembab, tuple_kritis):
    suhu_max, kelembaban_min = tuple_kritis

    if rata_suhu > suhu_max or rata_lembab < kelembaban_min:
        return "KRITIS: Nyalakan Pompa Irigasi!"
    return "NORMAL: Pompa Mati."
