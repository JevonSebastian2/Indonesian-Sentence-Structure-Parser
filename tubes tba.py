import streamlit as st

st.markdown('<h1 style="color: red;">Tugas Besar Teori Bahasa dan Automata!</h1>', unsafe_allow_html=True)
st.markdown("""
**Anggota Kelompok:**\n
Rangga Athari Gunawan (1301223185)\n
Rafi Aqil Kukuh Daffana (1301223060)\n
Jevon Sebastian (1301223391)\n
            
IF-46-10
            
**Deskripsi:** 
\nBuatlah sebuah parser sederhana untuk memeriksa kevalidan struktur kalimat berbahasa Indonesia. Struktur kalimat yang dikenali adalah kalimat berita aktif dengan struktur:
S – P – O – K ,
S – P – K ,
S – P – O ,
S – P ,
Adapun jenis subyek, predikat, obyek dan keterangan yang dikenali ditentukan oleh kelompok masing-masing dengan jumlah kata masing- masing sebanyak 5.\n
\n\n
Tanggal pengumpulan: 18 Juni 2024  jam 23.59 di LMS. \n\n

Pilihan Kata : \n
Subjek (S): anda, ayah, saya, kamu, ibu \n
Predikat (P): melihat, membawa, menulis, menendang, melempar \n
Objek (O): uang, buku, tas, bola, sepatu \n
Keterangan (K): di rumah, di sekolah, di kamar, besok, kemarin \n
            
""")
st.write('')

kalimat = st.text_input("Masukkan Kalimat:")
alpabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

ListState = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10',
              'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q6699',
              'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30',
              'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40',
              'q41', 'q42', 'q43', 'q44', 'q45', 'q46', 'q47', 'q48', 'q49', 'q50', 'q791', 'q792', 'q611', 'q612', 
              'q51', 'q52', 'q53', 'q54', 'q55', 'q56', 'q57', 'q58', 'q59', 'q60', 'q191', 'q192', 'q193', 'q194',
              'q61', 'q62', 'q63', 'q64', 'q65', 'q66', 'q67', 'q68', 'q69', 'q70', 'q312', 'q313', 'q313', 'q314', 'q129',
              'q71', 'q72', 'q73', 'q74', 'q75', 'q76', 'q77', 'q78', 'q79', 'q80', 'q301', 'q302', 'q303', 'q304', 'q501', 'q502', 'q511', 'q512', 'q513', 'q514', 'q515']

TransitionTable = {}
ParseTable = {}

for state in ListState:
    for alp in alpabet:
        TransitionTable[(state, alp)] = 'error'
    TransitionTable[(state, ' ')] = 'error'
    TransitionTable[(state, '#')] = 'error'

TransitionTable[('q0', 'a')] = 'q1'
TransitionTable[('q0', 's')] = 'q7' 
TransitionTable[('q0', 'i')] = 'q3'
TransitionTable[('q0', 'm')] = 'q4'
TransitionTable[('q0', 'b')] = 'q5'
TransitionTable[('q0', 'u')] = 'q6'
TransitionTable[('q0', 'k')] = 'q8'
TransitionTable[('q0', 'd')] = 'q9'
TransitionTable[('q0', 't')] = 'q10'
TransitionTable[('q1', 'y')] = 'q11'
TransitionTable[('q1', 'n')] = 'q12'
TransitionTable[('q7', 'a')] = 'q17' 
TransitionTable[('q7', 'i')] = 'q19'
TransitionTable[('q7', 'e')] = 'q191'
TransitionTable[('q191', 'p')] = 'q192'
TransitionTable[('q192', 'a')] = 'q193'
TransitionTable[('q193', 't')] = 'q194'
TransitionTable[('q194', 'u')] = 'q53'
TransitionTable[('q3', 'b')] = 'q22'
TransitionTable[('q4', 'e')] = 'q23'
TransitionTable[('q5', 'e')] = 'q39'
TransitionTable[('q5', 'u')] = 'q42'
TransitionTable[('q5', 'o')] = 'q43'
TransitionTable[('q6', 'a')] = 'q46'
TransitionTable[('q7', 'u')] = 'q48'
TransitionTable[('q8', 'i')] = 'q51'
TransitionTable[('q8', 'a')] = 'q501'
TransitionTable[('q501', 'm')] = 'q502'
TransitionTable[('q502', 'u')] = 'q21'
TransitionTable[('q8', 'e')] = 'q54'
TransitionTable[('q9', 'i')] = 'q59'
TransitionTable[('q10', 'a')] = 'q129'
TransitionTable[('q129', 's')] = 'q53'
TransitionTable[('q11', 'a')] = 'q13'
TransitionTable[('q13', 'h')] = 'q21'
TransitionTable[('q12', 'd')] = 'q14'
TransitionTable[('q14', 'a')] = 'q21'
TransitionTable[('q15', 'n')] = 'q16'
TransitionTable[('q16', 'g')] = 'q21'
TransitionTable[('q17', 'y')] = 'q18'
TransitionTable[('q18', 'a')] = 'q21'
TransitionTable[('q19', 's')] = 'q20'
TransitionTable[('q20', 'w')] = 'q18'
TransitionTable[('q22', 'u')] = 'q21'
TransitionTable[('q21', ' ')] = 'q0'
TransitionTable[('q23', 'm')] = 'q24'
TransitionTable[('q23', 'l')] = 'q301'
TransitionTable[('q301', 'i')] = 'q302'
TransitionTable[('q302', 'h')] = 'q303'
TransitionTable[('q303', 'a')] = 'q304'
TransitionTable[('q304', 't')] = 'q41'
TransitionTable[('q301', 'e')] = 'q312'
TransitionTable[('q312', 'm')] = 'q322'
TransitionTable[('q322', 'p')] = 'q332'
TransitionTable[('q332', 'a')] = 'q342'
TransitionTable[('q342', 'r')] = 'q41'
TransitionTable[('q23', 'n')] = 'q25'
TransitionTable[('q24', 'a')] = 'q26'
TransitionTable[('q24', 'b')] = 'q27'
TransitionTable[('q26', 's')] = 'q28'
TransitionTable[('q28', 'a')] = 'q30'
TransitionTable[('q30', 'k')] = 'q41'
TransitionTable[('q27', 'a')] = 'q29'
TransitionTable[('q29', 'w')] = 'q31'
TransitionTable[('q31', 'a')] = 'q41'
TransitionTable[('q25', 'u')] = 'q32'
TransitionTable[('q25', 'e')] = 'q511'
TransitionTable[('q511', 'n')] = 'q512'
TransitionTable[('q512', 'd')] = 'q513'
TransitionTable[('q513', 'a')] = 'q514'
TransitionTable[('q514', 'n')] = 'q515'
TransitionTable[('q515', 'g')] = 'q41'
TransitionTable[('q32', 'l')] = 'q34'
TransitionTable[('q34', 'i')] = 'q36'
TransitionTable[('q36', 's')] = 'q41'
TransitionTable[('q33', 'e')] = 'q35'
TransitionTable[('q35', 'j')] = 'q37'
TransitionTable[('q37', 'a')] = 'q38'
TransitionTable[('q38', 'r')] = 'q41'
TransitionTable[('q39', 'l')] = 'q40'
TransitionTable[('q39', 's')] = 'q611'
TransitionTable[('q611', 'o')] = 'q612'
TransitionTable[('q612', 'k')] = 'q79'
TransitionTable[('q40', 'a')] = 'q35'
TransitionTable[('q41', ' ')] = 'q0'
TransitionTable[('q42', 'k')] = 'q44'
TransitionTable[('q44', 'u')] = 'q53'
TransitionTable[('q43', 'l')] = 'q45'
TransitionTable[('q45', 'a')] = 'q53'
TransitionTable[('q46', 'n')] = 'q47'
TransitionTable[('q47', 'g')] = 'q53'
TransitionTable[('q48', 'r')] = 'q49'
TransitionTable[('q49', 'a')] = 'q50'
TransitionTable[('q50', 't')] = 'q53'
TransitionTable[('q51', 'm')] = 'q52'
TransitionTable[('q52', 'i')] = 'q80'
TransitionTable[('q80', 'a')] = 'q53'
TransitionTable[('q53', ' ')] = 'q0'
TransitionTable[('q54', 'm')] = 'q55'
TransitionTable[('q55', 'a')] = 'q56'
TransitionTable[('q56', 'r')] = 'q57'
TransitionTable[('q57', 'i')] = 'q58'
TransitionTable[('q58', 'n')] = 'q79'
TransitionTable[('q59', ' ')] = 'q60'
TransitionTable[('q60', 'r')] = 'q61'
TransitionTable[('q60', 'k')] = 'q62'
TransitionTable[('q60', 's')] = 'q63'
TransitionTable[('q61', 'u')] = 'q64'
TransitionTable[('q64', 'm')] = 'q65'
TransitionTable[('q65', 'a')] = 'q66'
TransitionTable[('q66', 'h')] = 'q79'
TransitionTable[('q62', 'a')] = 'q67'
TransitionTable[('q67', 'm')] = 'q68'
TransitionTable[('q68', 'a')] = 'q6699'
TransitionTable[('q6699', 'r')] = 'q79'
TransitionTable[('q63', 'e')] = 'q69'
TransitionTable[('q69', 'k')] = 'q70'
TransitionTable[('q70', 'o')] = 'q71'
TransitionTable[('q71', 'l')] = 'q791'
TransitionTable[('q791', 'a')] = 'q792'
TransitionTable[('q792', 'h')] = 'q79'
TransitionTable[('q72', 'd')] = 'q73'
TransitionTable[('q73', 'i')] = 'q74'
TransitionTable[('q74', ' ')] = 'q75'
TransitionTable[('q75', 'p')] = 'q76'
TransitionTable[('q76', 'a')] = 'q77'
TransitionTable[('q77', 'g')] = 'q78'
TransitionTable[('q78', 'i')] = 'q79'
TransitionTable[('q79', ' ')] = 'q0'
ParseTable[('START', 'ibu')] = ['S']
ParseTable[('START', 'ayah')] = ['S']
ParseTable[('START', 'anda')] = ['S']
ParseTable[('START', 'kamu')] = ['S']
ParseTable[('START', 'saya')] = ['S']
ParseTable[('START', 'melihat')] = ['error']
ParseTable[('START', 'mambawa')] = ['error']
ParseTable[('START', 'menulis')] = ['error']
ParseTable[('START', 'menendang')] = ['error']
ParseTable[('START', 'melempar')] = ['error']
ParseTable[('START', 'uang')] = ['error']
ParseTable[('START', 'buku')] = ['error']
ParseTable[('START', 'tas')] = ['error']
ParseTable[('START', 'bola')] = ['error']
ParseTable[('START', 'sepatu')] = ['error']
ParseTable[('START', 'dirumah')] = ['error']
ParseTable[('START', 'disekolah')] = ['error']
ParseTable[('START', 'dikamar')] = ['error']
ParseTable[('START', 'besok')] = ['error']
ParseTable[('START', 'kemarin')] = ['error']
ParseTable[('START', 'EOS')] = ['error']
ParseTable[('S', 'ibu')] = ['ibu', 'P']
ParseTable[('S', 'ayah')] = ['ayah', 'P']
ParseTable[('S', 'anda')] = ['anda', 'P']
ParseTable[('S', 'kamu')] = ['kamu', 'P']
ParseTable[('S', 'saya')] = ['saya', 'P']
ParseTable[('S', 'melihat')] = ['error']
ParseTable[('S', 'mambawa')] = ['error']
ParseTable[('S', 'menulis')] = ['error']
ParseTable[('S', 'menendang')] = ['error']
ParseTable[('S', 'melempar')] = ['error']
ParseTable[('S', 'uang')] = ['error']
ParseTable[('S', 'buku')] = ['error']
ParseTable[('S', 'tas')] = ['error']
ParseTable[('S', 'bola')] = ['error']
ParseTable[('S', 'sepatu')] = ['error']
ParseTable[('S', 'dirumah')] = ['error']
ParseTable[('S', 'disekolah')] = ['error']
ParseTable[('S', 'dikamar')] = ['error']
ParseTable[('S', 'besok')] = ['error']
ParseTable[('S', 'kemarin')] = ['error']
ParseTable[('S', 'EOS')] = ['error']
ParseTable[('P', 'ibu')] = ['error']
ParseTable[('P', 'ayah')] = ['error']
ParseTable[('P', 'anda')] = ['error']
ParseTable[('P', 'kamu')] = ['error']
ParseTable[('P', 'saya')] = ['error']
ParseTable[('P', 'melihat')] = ['melihat', 'O']
ParseTable[('P', 'mambawa')] = ['mambawa', 'O']
ParseTable[('P', 'menulis')] = ['menulis', 'O']
ParseTable[('P', 'menendang')] = ['menendang', 'O']
ParseTable[('P', 'melempar')] = ['melempar', 'O']
ParseTable[('P', 'uang')] = ['error']
ParseTable[('P', 'buku')] = ['error']
ParseTable[('P', 'tas')] = ['error']
ParseTable[('P', 'bola')] = ['error']
ParseTable[('P', 'sepatu')] = ['error']
ParseTable[('P', 'dirumah')] = ['error']
ParseTable[('P', 'disekolah')] = ['error']
ParseTable[('P', 'dikamar')] = ['error']
ParseTable[('P', 'besok')] = ['error']
ParseTable[('P', 'kemarin')] = ['error']
ParseTable[('P', 'EOS')] = ['error']
ParseTable[('O', 'ibu')] = ['error']
ParseTable[('O', 'ayah')] = ['error']
ParseTable[('O', 'anda')] = ['error']
ParseTable[('O', 'kamu')] = ['error']
ParseTable[('O', 'saya')] = ['error']
ParseTable[('O', 'melihat')] = ['error']
ParseTable[('O', 'mambawa')] = ['error']
ParseTable[('O', 'menulis')] = ['error']
ParseTable[('O', 'menendang')] = ['error']
ParseTable[('O', 'melempar')] = ['error']
ParseTable[('O', 'uang')] = ['uang', 'K']
ParseTable[('O', 'buku')] = ['buku', 'K']
ParseTable[('O', 'tas')] = ['tas', 'K']
ParseTable[('O', 'bola')] = ['bola', 'K']
ParseTable[('O', 'sepatu')] = ['sepatu', 'K']
ParseTable[('O', 'dirumah')] = ['K']
ParseTable[('O', 'disekolah')] = ['K']
ParseTable[('O', 'dikamar')] = ['K']
ParseTable[('O', 'besok')] = ['K']
ParseTable[('O', 'kemarin')] = ['K']
ParseTable[('O', 'EOS')] = ['epsilon']
ParseTable[('K', 'ibu')] = ['error']
ParseTable[('K', 'ayah')] = ['error']
ParseTable[('K', 'anda')] = ['error']
ParseTable[('K', 'kamu')] = ['error']
ParseTable[('K', 'saya')] = ['error']
ParseTable[('K', 'melihat')] = ['error']
ParseTable[('K', 'mambawa')] = ['error']
ParseTable[('K', 'menulis')] = ['error']
ParseTable[('K', 'menendang')] = ['error']
ParseTable[('K', 'melempar')] = ['error']
ParseTable[('K', 'uang')] = ['error']
ParseTable[('K', 'buku')] = ['error']
ParseTable[('K', 'tas')] = ['error']
ParseTable[('K', 'bola')] = ['error']
ParseTable[('K', 'sepatu')] = ['error']
ParseTable[('K', 'dirumah')] = ['dirumah']
ParseTable[('K', 'disekolah')] = ['disekolah']
ParseTable[('K', 'dikamar')] = ['dikamar']
ParseTable[('K', 'besok')] = ['besok']
ParseTable[('K', 'kemarin')] = ['kemarin']
ParseTable[('K', 'EOS')] = ['epsilon']

if kalimat:
    st.write("--------------------------------------------------------")
    st.markdown('<h2 style="color: red;">Token Recognizer</h2>', unsafe_allow_html=True)

    st.write("--------------------------------------------------------")

    tokens = []
    token = ""
    state = 'q0'
    temp = kalimat+'#' 
    struktur = []
    for i in range(len(temp)):
        if temp[i] != ' ':
            token += temp[i]
        state = TransitionTable[(state, temp[i])]
        if state == 'q21':
            st.write(f'Token: "{token}" , Kata tersebut merupakan SUBJEK')
            struktur.append('Subjek')
            tokens.append(token)
            token = ""
        elif state == 'q41':
            st.write(f'Token: "{token}" , Kata tersebut merupakan PREDIKAT')
            struktur.append('Predikat')
            tokens.append(token)
            token = ""
        elif state == 'q53':
            st.write(f'Token: "{token}" , Kata tersebut merupakan OBJEK')
            struktur.append('Objek')
            tokens.append(token)
            token = ""
        elif state == 'q79':
            st.write(f'Token: "{token}" , Kata tersebut merupakan KETERANGAN')
            struktur.append('Keterangan')
            tokens.append(token)
            token = ""
        
        if state == 'error' and temp[i] == '#':
            valid = True
            break
        elif state == 'error':
            st.write("index", i)
            i+=1
            while True:
                if temp[i] == ' ' or temp[i] == '#':
                    break
                token += temp[i]
                i+=1
            valid = False
            break
    st.write("--------------------------------------------------------")
    if valid:
        st.write(f'\n  Kata-kata  "{kalimat}" adalah benar')
        st.write(f"Token: {tokens}")
    else:
        st.write(f'\ Kesalahan kata dalam "{kalimat}", kata "{token}" tidak termasuk dalam data SPOK')

    # PARSER PDA
    tokens.append("EOS")
    stack = []
    nonterminal = ['START', 'S', 'P', 'O', 'K']
    terminal = ['ibu', 'ayah', 'anda', 'kamu', 'saya', 'melihat', 'mambawa', 'menulis', 'menendang', 'melempar', 'uang', 'buku', 'tas', 'bola', 'sepatu', 'dirumah', 'disekolah', 'dikamar', 'besok', 'kemarin', 'EOS', 'epsilon']

    stack.append('#')
    stack.append('START')

    st.write("\n-----------------------------------------------------------------")
    st.markdown('<h2 style="color: red;">Parser Push Down Automata</h2>', unsafe_allow_html=True)

    st.write("-----------------------------------------------------------------")

    indeks = 0
    while True:
        if stack[-1] in terminal:
            st.write(f"\nStack: {stack}")
            st.write("Top Stack: ", stack[-1], "(Variabel Terminal)")
            
            if stack[-1] == tokens[indeks]:
                st.write(f'Token: "{tokens[indeks]}" Ditemukan')
                st.write("\n--------------------------------------------------------")
                stack.pop()
                indeks += 1
            elif stack[-1] == 'epsilon':
                st.write('Epsilon ditemukan')
                stack.pop()
            else:
                st.write(f'Token: "{tokens[indeks]}" Tidak Ditemukan')
                break
        elif stack[-1] in nonterminal:
            st.write(f"\nStack: {stack}")
            st.write("Top Stack: ", stack[-1], "(Variabel Non-Terminal)")
            
            st.write("\n--------------------------------------------------------")
            temp = ParseTable[(stack[-1], tokens[indeks])]
            stack.pop()
            for i in range(len(temp)):
                stack.append(temp[len(temp)-1-i])
        elif stack[-1] == 'error':
            st.write(f'\Terdapat kesalahan, kalimat "{kalimat}" tidak sesuai SPOK')
            break
        elif stack[-1] == '#':
            if tokens[indeks] == "EOS":
                st.write(f'**Benar, kalimat "{kalimat}"  sesuai dengan SPOK. Strukur: {struktur}**')
            else:
                st.write(f'**Terdapat kesalahan, kalimat "{kalimat}" tidak sesuai SPOK**')
            break

    st.write("\n--------------------------------------------------------")