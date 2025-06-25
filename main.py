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
        "music": [("Hans Zimmer - Time", "https://www.youtube.com/watch?v=RxabLA7UQ9k")]
    },
    "INTP": {
        "movies": ["소셜 네트워크", "굿 윌 헌팅", "매트릭스", "아이로봇"],
        "music": [("Radiohead - No Surprises", "https://www.youtube.com/watch?v=u5CVsCnxyXg")]
    },
    "ENTJ": {
        "movies": ["월 스트리트", "인턴", "킹스맨", "머니볼"],
        "music": [("Imagine Dragons - Believer", "https://www.youtube.com/watch?v=7wtfhZwyrcc")]
    },
    "ENTP": {
        "movies": ["아이언맨", "셜록 홈즈", "조커", "위대한 쇼맨"],
        "music": [("Panic! At The Disco - High Hopes", "https://www.youtube.com/watch?v=IPXIgEAGe4U")]
    },
    "INFJ": {
        "movies": ["비포 선라이즈", "그린북", "트루먼 쇼", "라이프 오브 파이"],
        "music": [("Sufjan Stevens - Mystery of Love", "https://www.youtube.com/watch?v=3Uqv1fHLtmg")]
    },
    "INFP": {
        "movies": ["이터널 선샤인", "월플라워", "비긴 어게인", "어바웃 타임"],
        "music": [("Lauv - I Like Me Better", "https://www.youtube.com/watch?v=B3eAMGXFw1o")]
    },
    "ENFJ": {
        "movies": ["타이타닉", "원스", "드림걸즈", "굿 윌 헌팅"],
        "music": [("John Legend - All of Me", "https://www.youtube.com/watch?v=450p7goxZqg")]
    },
    "ENFP": {
        "movies": ["포레스트 검프", "라라랜드", "인턴", "주토피아"],
        "music": [("Coldplay - Viva La Vida", "https://www.youtube.com/watch?v=dvgZkm1xWPE")]
    },
    "ISTJ": {
        "movies": ["셜록 홈즈", "캐치 미 이프 유 캔", "본 아이덴티티", "그레이 맨"],
        "music": [("Beethoven - Symphony No.5", "https://www.youtube.com/watch?v=fOk8Tm815lE")]
    },
    "ISFJ": {
        "movies": ["작은 아씨들", "업", "말할 수 없는 비밀", "인사이드 아웃"],
        "music": [("BTS - Spring Day", "https://www.youtube.com/watch?v=xEeFrLSkMm8")]
    },
    "ESTJ": {
        "movies": ["미션 임파서블", "월 스트리트", "블랙 팬서", "다크 나이트"],
        "music": [("Survivor - Eye of the Tiger", "https://www.youtube.com/watch?v=btPJPFnesV4")]
    },
    "ESFJ": {
        "movies": ["맘마미아!", "노트북", "러브 액츄얼리", "업"],
        "music": [("Celine Dion - My Heart Will Go On", "https://www.youtube.com/watch?v=FHG2oizTlpY")]
    },
    "ISTP": {
        "movies": ["본 시리즈", "인터스텔라", "007", "인셉션"],
        "music": [("Daft Punk - Derezzed", "https://www.youtube.com/watch?v=m4cgLL8JaVI")]
    },
    "ISFP": {
        "movies": ["아멜리에", "코코", "비긴 어게인", "라라랜드"],
        "music": [("Ed Sheeran - Perfect", "https://www.youtube.com/watch?v=2Vv-BfVoq4g")]
    },
    "ESTP": {
        "movies": ["분노의 질주", "베이비 드라이버", "킹스맨", "미션 임파서블"],
        "music": [("Pitbull - Fireball", "https://www.youtube.com/watch?v=HMqgVXSvwGo")]
    },
    "ESFP": {
        "movies": ["위대한 쇼맨", "맘마미아!", "인크레더블", "주토피아"],
        "music": [("Bruno Mars - 24K Magic", "https://www.youtube.com/watch?v=UqyT8IEBkvY")]
    }
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

    if mbti in recommendations:
    st.markdown(f"## {emojis.get(mbti, '')} {mbti} 추천 콘텐츠")

    st.subheader("🎬 영화 추천")
    for movie in recommendations[mbti].get("movies", []):
        st.markdown(f"**{movie['title']}**")
        st.image(movie["poster"], use_column_width=True)

    st.subheader("🎵 음악 추천")
    for title, url in recommendations[mbti].get("music", []):
        st.markdown(f"[{title}]({url})")
else:
    st.warning("이 MBTI에 대한 추천 정보가 아직 없어요. 곧 추가할게요!")

# 🔁 다시 추천 버튼
if st.button("다시 추천해줘 🔄"):
    st.rerun()
