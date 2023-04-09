import json
import requests

class TCDogrulama:
    def tcKimlik(self, tc, ad, soyad, ay, gun, yil):
        if not self.identityVerify(tc):
            return {
                'success': False,
                'obj': {
                    'HataAciklama': 'T.C Kimlik Numaranız Hatalı'
                }
            }

        if not self.nameString(ad):
            return {
                'success': False,
                'obj': {
                    'HataAciklama': 'Ad Sadece Karakter Olabilir.'
                }
            }

        TCDogrulama = {
            "TCKimlikNo": tc,
            "Ad": ad,
            "Soyad": soyad,
            "DogumAy": ay,
            "DogumGun": gun,
            "DogumYil": yil
        }

        response = requests.post('https://tckimlik.nvi.gov.tr/tcKimlikNoDogrula/search', data=TCDogrulama)

        return response.json()

    def identityVerify(self, id):
        if len(id) != 11:
            return False
        return True

    def nameString(self, name):
        if isinstance(name, str) == False:
            return False
        return True

a = TCDogrulama()
data = a.tcKimlik('tcggir', 'adgir', 'soyadgir', 'aygir', 'gungir', 'yilgir')

with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)
