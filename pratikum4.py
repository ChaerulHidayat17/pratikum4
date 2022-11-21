dataMahasiswa = []

while True:

    print('===========================================================================')
    print('=========================== PROGRAM =======================================')
    print(' ================== INPUT DATA NILAI MAHASIWA ============================ ')
    print('=====================================================================c======')

    nama = (input(" Masukan Nama Mahasiswa    : "))
    nim = int(input(" Masukan NIM Mahasiswa     : "))
    tugas = int(input(" Masuka Nilai tugas       : "))
    uts = int(input("Masukan Nilai UTS         : "))
    uas = int(input("Masukan Nilai UAS         : "))
    print('====================================')

    akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

    dataMahasiswa.append([nama, nim, tugas, uts, uas, akhir])
    pilihan = (input("Tambah Data (ya/tidak)? "))
    print()
    if pilihan == 'ya':
        continue
    elif pilihan == "tidak":
        break
print("===================================================================================================")
print("| No |          Nama          |       NIM       |   Tugas   |   UTS   |   UAS   |   Nilai Akhir   |")
print("===================================================================================================")

i = 0
for c in dataMahasiswa:
    i += 1
    print("| {no:2d} | {nama:22s} | {nim:15d} | {tugas:9d} | {uts:7d} | {uas:7d} | {akhir:15f} |".format(no=i, nama=c[0], nim=c[1], tugas=c[2], uts=c[3], uas=c[4], akhir=c[5]))

print("===================================================================================================")




