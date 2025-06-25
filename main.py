import streamlit as st
import random

st.set_page_config(page_title="MBTI 추천 앱", layout="centered")

st.title("🎬🎵 MBTI별 추천 영화 & 음악 앱")
st.write("당신의 MBTI에 따라 영화와 음악을 추천해드려요!")

# 🎭 MBTI별 이모지 설정
mbti_emojis = {
    "INTJ": "🧠", "INTP": "🔍", "ENTJ": "📈", "ENTP": "💡",
    "INFJ": "🕊️", "INFP": "🌸", "ENFJ": "🤝", "ENFP": "🔥",
    "ISTJ": "📘", "ISFJ": "🧸", "ESTJ": "📊", "ESFJ": "🎀",
    "ISTP": "🛠️", "ISFP": "🎨", "ESTP": "⚡", "ESFP": "🎉"
}

# 🎬 + 🎵 MBTI별 추천 데이터 (유튜브 링크 포함)
recommendations = {
    "INTJ": {
        "movies": ["인셉션", "인터스텔라", "셜록", "매트릭스"],
        "music": [("Hans Zimmer - Time", "https://www.youtube.com/watch?v=RxabLA7UQ9k"),
                  ("Radiohead - Everything in Its Right Place", "https://www.youtube.com/watch?v=onRk0sjSgFU")]
    },
    "INFP": {
        "movies": ["이터널 선샤인", "월플라워", "비긴 어게인", "어바웃 타임"],
        "music": [("Lauv - I Like Me Better", "https://www.youtube.com/watch?v=B3eAMGXFw1o"),
                  ("Lana Del Rey - Young and Beautiful", "https://www.youtube.com/watch?v=o_1aF54DO60")]
    },
    "ENFP": {
        "movies": ["포레스트 검프", "라라랜드", "인턴", "주토피아"],
        "music": [("Coldplay - Viva La Vida", "https://www.youtube.com/watch?v=dvgZkm1xWPE"),
                  ("Owl City - Fireflies", "https://www.youtube.com/watch?v=psuRGfAaju4")]
    },
    "ISFJ": {
        "movies": ["작은 아씨들", "업", "말할 수 없는 비밀", "인사이드 아웃"],
        "music": [("BTS - Spring Day", "https://www.youtube.com/watch?v=xEeFrLSkMm8"),
                  ("Adele - Easy On Me", "https://www.youtube.com/watch?v=U3ASj1L6_sY")]
    },
    # 다른 MBTI들도 같은 형식으로 추가 가능!
}

# 🎨 파스텔톤 배경색
mbti_colors = {
    "INTJ": "#cce2cb", "INTP": "#d0e6f6", "ENTJ": "#f8d1c9", "ENTP": "#fce1e4",
    "INFJ": "#e4c1f9", "INFP": "#ffd6e0", "ENFJ": "#fff1bd", "ENFP": "#ffecd1",
    "ISTJ": "#d9f0ff", "ISFJ": "#f3ffe3", "ESTJ": "#ffe0ac", "ESFJ": "#ffe5ec",
    "ISTP": "#e0f7fa", "ISFP": "#f6dfeb", "ESTP": "#fff0f5", "ESFP": "#f9fbe7"
}

# 👤 사용자 MBTI 입력
mbti_list = list(mbti_emojis.keys())
user_mbti = st.selectbox("당신의 MBTI를 선택하세요 👇", mbti_list)

# 💄 스타일 설정
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
            a {{
                color: #007acc;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

    emoji = mbti_emojis.get(user_mbti, "")
    st.header(f"{emoji} {user_mbti} 유형을 위한 추천")

    if user_mbti in recommendations:
        movie = random.choice(recommendations[user_mbti]["movies"])
        music_title, music_url = random.choice(recommendations[user_mbti]["music"])

        st.subheader("🎬 추천 영화")
        st.success(movie)

        st.subheader("🎵 추천 음악")
        st.markdown(f"✅ [{music_title}]({music_url})", unsafe_allow_html=True)
    else:
        st.warning("이 MBTI에 대한 추천 정보가 아직 없어요. 곧 추가할게요!")

# 🔁 다시 추천 버튼
if st.button("다시 추천해줘 🔄"):
    st.rerun()
