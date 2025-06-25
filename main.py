import streamlit as st
import random

st.set_page_config(page_title="MBTI 추천 앱", layout="centered")

st.title("🎬🎵 MBTI별 추천 영화 & 음악 앱")
st.write("당신의 MBTI에 따라 영화와 음악을 추천해드려요!")

# MBTI별 추천 데이터
recommendations = {
    "INTJ": {
        "movies": ["인셉션", "인터스텔라", "셜록", "매트릭스"],
        "music": ["Hans Zimmer - Time", "Radiohead - Everything in Its Right Place"]
    },
    "INFP": {
        "movies": ["이터널 선샤인", "월플라워", "비긴 어게인", "어바웃 타임"],
        "music": ["Lauv - I Like Me Better", "Lana Del Rey - Young and Beautiful"]
    },
    "ENTP": {
        "movies": ["소셜 네트워크", "아이언맨", "빅쇼트", "울프 오브 월 스트리트"],
        "music": ["Imagine Dragons - Thunder", "Kanye West - Stronger"]
    },
    "ISFJ": {
        "movies": ["작은 아씨들", "업", "말할 수 없는 비밀", "인사이드 아웃"],
        "music": ["BTS - Spring Day", "Adele - Easy On Me"]
    },
    "ENFP": {
        "movies": ["포레스트 검프", "라라랜드", "인턴", "주토피아"],
        "music": ["Coldplay - Viva La Vida", "Owl City - Fireflies"]
    },
    "ISTP": {
        "movies": ["본 아이덴티티", "존 윅", "미션 임파서블", "드라이브"],
        "music": ["The Weeknd - Blinding Lights", "Daft Punk - Harder Better Faster Stronger"]
    },
    "ESFJ": {
        "movies": ["크루엘라", "프린세스 다이어리", "맘마미아!", "노팅힐"],
        "music": ["Taylor Swift - Shake It Off", "Bruno Mars - Just the Way You Are"]
    },
    "INFJ": {
        "movies": ["가타카", "인사이드 르윈", "노마드랜드", "그랜드 부다페스트 호텔"],
        "music": ["Aurora - Runaway", "Sufjan Stevens - Mystery of Love"]
    },
    "ESTJ": {
        "movies": ["머니볼", "캐치 미 이프 유 캔", "설국열차", "글래디에이터"],
        "music": ["Survivor - Eye of the Tiger", "Imagine Dragons - Believer"]
    },
    "INTP": {
        "movies": ["엑스 마키나", "트루먼 쇼", "인터스텔라", "셜록 홈즈"],
        "music": ["Muse - Starlight", "Pink Floyd - Time"]
    },
    "ENFJ": {
        "movies": ["라이온 킹", "사운드 오브 뮤직", "코코", "월E"],
        "music": ["Beyoncé - Halo", "John Legend - All of Me"]
    },
    "ISTJ": {
        "movies": ["다크 나이트", "세븐", "인셉션", "캐치 미 이프 유 캔"],
        "music": ["Linkin Park - Numb", "Eminem - Lose Yourself"]
    },
    "ISFP": {
        "movies": ["콜 미 바이 유어 네임", "비포 선라이즈", "캐롤", "그녀"],
        "music": ["Billie Eilish - Ocean Eyes", "Lorde - Royals"]
    },
    "ESFP": {
        "movies": ["위대한 쇼맨", "맘마미아!", "씽", "라푼젤"],
        "music": ["Dua Lipa - Levitating", "Lady Gaga - Born This Way"]
    },
    "ENTJ": {
        "movies": ["울프 오브 월 스트리트", "소셜 네트워크", "스티브 잡스", "인셉션"],
        "music": ["Kanye West - Power", "Jay-Z - Empire State of Mind"]
    },
    "ESTP": {
        "movies": ["분노의 질주", "존 윅", "매드 맥스: 분노의 도로", "킹스맨"],
        "music": ["AC/DC - Thunderstruck", "Pitbull - Timber"]
    },
}

# 파스텔톤 배경색
mbti_colors = {
    "INTJ": "#cce2cb", "INTP": "#d0e6f6", "ENTJ": "#f8d1c9", "ENTP": "#fce1e4",
    "INFJ": "#e4c1f9", "INFP": "#ffd6e0", "ENFJ": "#fff1bd", "ENFP": "#ffecd1",
    "ISTJ": "#d9f0ff", "ISFJ": "#f3ffe3", "ESTJ": "#ffe0ac", "ESFJ": "#ffe5ec",
    "ISTP": "#e0f7fa", "ISFP": "#f6dfeb", "ESTP": "#fff0f5", "ESFP": "#f9fbe7"
}

mbti_list = list(recommendations.keys())
user_mbti = st.selectbox("당신의 MBTI를 선택하세요 👇", mbti_list)

# 배경색 + 글자색 설정
if user_mbti:
    bg_color = mbti_colors.get(user_mbti, "#ffffff")
    st.markdown(
        f"""
        <style>
            .stApp {{
                background-color: {bg_color};
                color: black;
            }}
            h1, h2, h3, h4, h5, h6, p, label {{
                color: black !important;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

    if user_mbti in recommendations:
        movie = random.choice(recommendations[user_mbti]["movies"])
        music = random.choice(recommendations[user_mbti]["music"])
        st.subheader(f"🎬 {user_mbti} 유형을 위한 추천 영화:")
        st.success(movie)
        st.subheader(f"🎵 {user_mbti} 유형을 위한 추천 음악:")
        st.success(music)
    else:
        st.warning("이 MBTI에 대한 추천 정보가 아직 없어요. 곧 추가할게요!")

# 다시 추천 버튼
if st.button("다시 추천해줘 🔄"):
    st.rerun()
