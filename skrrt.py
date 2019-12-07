import streamlit as st

def masukkan_audio(file_name):
    return open(file_name,'rb').read()

def mp3(audio_bytes):
    audio_byte = masukkan_audio(audio_bytes)
    format_ = audio_bytes.split('.')[-1]
    return st.audio(audio_byte, format=f'audio/{format_}')

st.markdown('# welcome operator')
st.markdown('---')
st.write('untuk startnya tunggu aba-aba')
st.write('untuk selesainya menyesuaikan waktu selesai-nya saja')

st.markdown('---')
st.write('jangan lupa untuk dimatikan terlebih dahulu file yang sudah di play')

st.markdown('---')
st.markdown('## start here')


st.info('masuk ironman')
mp3('ironman_masuk_1.mp3')

st.info('masuk flash')
mp3('flash_masuk_1.wav')

st.info('masuk captain america')
mp3('captainamerica_masuk_1.wav')

st.info('antman masuk')
mp3('antman_masuk_1.wav')

st.info('antman ketika ada diandra masuk')
st.write('biarin aja, lanjut lagu antman sendiri')
mp3('antman_masuk_2.wav')

st.info('masuk thor')
mp3('thor_masuk_1.wav')
st.markdown('# PERANG broooo')
st.error('PERANG PERANG')
mp3('lagu_perang_2.wav')

st.markdown('# IZINKAN AKU')
st.error('tunggu sampai hezga maju ke depan')
mp3('koplo.wav')

st.markdown('# AKU MUNDUR ALON ALON')
st.error('tunggu sampai jonas "terjatuh"')
mp3('koplo_alon.wav')
