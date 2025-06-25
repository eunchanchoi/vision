import streamlit as st
import random

st.set_page_config(page_title="MBTI 추천기", layout="centered")

st.title("🎬 MBTI 기반 영화/음악 추천기")
st.subheader("당신의 성격이 좋아할 콘텐츠를 골라드릴게요!")

# MBTI 목록
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

user_mbti = st.selectbox("당신의 MBTI를 선택하세요 👇", mbti_list)

# 더미 추천 데이터
recommendations = {
    "INTJ": {
        "movies": [
            {"title": "인셉션", "desc": "복잡한 구조 속에서 통제하려는 전략가"},
            {"title": "셜록", "desc": "논리와 추리의 끝판왕"}
        ],
        "music": [
            {"title": "Hans Zimmer - Time", "url": "https://www.youtube.com/watch?v=RxabLA7UQ9k"},
            {"title": "Ludovico Einaudi - Experience", "url": "https://www.youtube.com/watch?v=91pFNA7n3LE"}
        ]
    },
    "ENFP": {
        "movies": [
            {"title": "월터의 상상은 현실이 된다", "desc": "모험을 사랑하는 낙천가"},
            {"title": "라라랜드", "desc": "꿈과 사랑을 향해"}
        ],
        "music": [
            {"title": "Coldplay - Adventure of a Lifetime", "url": "https://www.youtube.com/watch?v=QtXby3twMmI"},
            {"title": "BTS - Dynamite", "url": "https://www.youtube.com/watch?v=gdZLi9oWNZg"}
        ]
    },
    # ... 다른 유형도 추가 가능
}

if user_mbti in recommendations:
    movie = random.choice(recommendations[user_mbti]["movies"])
    music = random.choice(recommendations[user_mbti]["music"])

    st.write("🎥 **영화 추천**")
    st.markdown(f"**{movie['title']}** — {movie['desc']}")

    st.write("🎵 **음악 추천**")
    st.markdown(f"[{music['title']}]({music['url']})")

    if st.button("다시 추천해줘 🔄"):
        st.experimental_rerun()
else:
    st.warning("아직 이 MBTI에 대한 추천 정보가 없어요. 곧 추가할게요!")

