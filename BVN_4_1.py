# List
bangchucai = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']

def MaHoaCeasar(tencuaban, stt):
    chuoi = ""
    for ch in tencuaban:
        if ch.lower() in bangchucai:
            i = bangchucai.index(ch.lower())
            i2 = (i + stt) % len(bangchucai)
            
            if ch.isupper():
                chuoi += bangchucai[i2].upper()
            else:
                chuoi += bangchucai[i2]
        else:
            chuoi += ch
    return chuoi


# test
tencuaban = input("Nhap plaintext (Ten cua ban): ")
stt = int(input("Nhap so k (STT): "))

kq = MaHoaCeasar(tencuaban, stt)
print("Ten cua ban sau khi ma hoa:", kq)