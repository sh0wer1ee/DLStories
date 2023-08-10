# Test audio export
import json
import os
import sys
import subprocess
from pydub import AudioSegment

vgm_path = './vgmstream/test.exe'
cri_audio_dir = 'assets/localize.ja_jp.sound.v.story'
output_dir = 'audio/output'
mainstory_dir = 'audio/mainstory'
knightsstory_dir = 'audio/knightsstory'
eventstory_dir = 'audio/eventstory'
ingamestory_dir = 'audio/ingamestory'
output_file = '?n.wav'#'?03s.wav'

def convertCriAudioToWav():
    os.makedirs(output_dir, exist_ok=True)
    err_list = []
    for f in os.listdir(cri_audio_dir):
        if 'awb' in f:
            if 'vo_chr_mainstory_' in f or 'vo_chr_knightsstory_' in f or 'vo_chr_eventstory_' in f or 'vo_chr_ingamestory' in f:
                print(f'processing {f}...')
                audio_file = os.path.join(cri_audio_dir, f)
                data = {}
                count = 0
                try:
                    output = subprocess.check_output(f'{vgm_path} -I -m {audio_file}')
                    data = json.loads(output)
                    count = data['streamInfo']['total']
                    #name = data['streamInfo']['name']
                    #subprocess.check_output(f'{vgm_path} -s {count} -i -o {output_dir}/{output_file} {audio_file}').decode('utf-8')
                    for i in range(count):#i+1!!!!!
                        subprocess.check_output(f'{vgm_path} -s {i+1} -i -o {output_dir}/{output_file} {audio_file}').decode('utf-8')
                        #input()
                except subprocess.CalledProcessError as err:
                    err_list.append()
                    print(err)
    print(len(err_list))
    print(err_list)

def convertWavToMp3():
    os.makedirs(mainstory_dir, exist_ok=True)
    os.makedirs(knightsstory_dir, exist_ok=True)
    os.makedirs(eventstory_dir, exist_ok=True)
    os.makedirs(ingamestory_dir, exist_ok=True)
    for f in os.listdir(output_dir):
        if '.wav' in f:
            mp3_dir = ''
            wav_file = os.path.join(output_dir, f)
            print(f'processing {f}...')
            sp = f.split('_')
            if 'VO_CHR_MAINSTORY_' in f: 
                #vo_chr_mainstory_09_06 
                mp3_dir = os.path.join(mainstory_dir, f'{sp[3]}{sp[4]}')
                os.makedirs(mp3_dir, exist_ok=True)

            elif 'VO_CHR_KNIGHTSSTORY_' in f:
                #vo_chr_knightsstory_100002_13_02 00-04！！！
                mp3_dir = os.path.join(knightsstory_dir, f'{sp[3]}{sp[4]}{sp[5]}')
                os.makedirs(mp3_dir, exist_ok=True)
                
            elif 'VO_CHR_EVENTSTORY_' in f:
                #vo_chr_eventstory_20403_06
                mp3_dir = os.path.join(eventstory_dir, f'{sp[3]}{sp[4]}')
                os.makedirs(mp3_dir, exist_ok=True)
            elif 'VO_CHR_INGAMESTORY_' in f:
                #VO_CHR_INGAMESTORY_00_01_0001
                mp3_dir = os.path.join(ingamestory_dir, f'{sp[3]}{sp[4]}')
                os.makedirs(mp3_dir, exist_ok=True)
            else:
                print('???')
                exit()
            sound = AudioSegment.from_wav(wav_file)
            sound.export(os.path.join(mp3_dir, f.replace('.wav', '.mp3')), format="mp3")

def findDelim():
    for f in os.listdir(output_dir):
        if ';' in f:
            print(f)

if __name__ == '__main__':
    #convertCriAudioToWav()
    convertWavToMp3()
    #findDelim()
'''
√ VO_CHR_KNIGHTSSTORY_100002_01_03_0007; VO_CHR_KNIGHTSSTORY_100002_01_03_0041.wav
√ VO_CHR_KNIGHTSSTORY_100006_01_02_0052; VO_CHR_KNIGHTSSTORY_100006_01_02_0062.wav
√ VO_CHR_KNIGHTSSTORY_100006_01_02_0054; VO_CHR_KNIGHTSSTORY_100006_01_02_0063.wav
√ VO_CHR_KNIGHTSSTORY_100006_01_02_0055; VO_CHR_KNIGHTSSTORY_100006_01_02_0064.wav
√ VO_CHR_KNIGHTSSTORY_100006_01_02_0057; VO_CHR_KNIGHTSSTORY_100006_01_02_0065.wav
√ VO_CHR_KNIGHTSSTORY_100006_01_02_0059; VO_CHR_KNIGHTSSTORY_100006_01_02_0066.wav
√ VO_CHR_KNIGHTSSTORY_100006_01_04_0011; VO_CHR_KNIGHTSSTORY_100006_01_04_0050.wav
√ VO_CHR_KNIGHTSSTORY_100006_01_04_0014; VO_CHR_KNIGHTSSTORY_100006_01_04_0051.wav
√ VO_CHR_KNIGHTSSTORY_110021_01_03_0042; VO_CHR_KNIGHTSSTORY_110021_01_03_0044.wav
√ VO_CHR_KNIGHTSSTORY_110252_01_03_0024; VO_CHR_KNIGHTSSTORY_110252_01_03_0032.wav
√ VO_CHR_KNIGHTSSTORY_110252_01_04_0018; VO_CHR_KNIGHTSSTORY_110252_01_04_0033.wav
√ VO_CHR_MAINSTORY_01_07_0048; VO_CHR_MAINSTORY_01_07_1012.wav
'''