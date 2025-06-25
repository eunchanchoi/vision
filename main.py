import streamlit as st
import random

st.set_page_config(page_title="MBTI 추천기", layout="centered")
st.title("🎬 MBTI 기반 영화/음악 추천기")
st.subheader("당신의 성격이 좋아할 콘텐츠를 골라드릴게요!")

mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

recommendations = {
    "INTJ": {
        "movies": [{"title": "인셉션", "desc": "복잡한 구조 속에서도 통제하려는 전략가"},
                   {"title": "셜록", "desc": "논리와 추리의 끝판왕"}],
        "music": [{"title": "Hans Zimmer - Time", "url": "https://www.youtube.com/watch?v=RxabLA7UQ9k"},
                  {"title": "Ludovico Einaudi - Experience", "url": "https://www.youtube.com/watch?v=91pFNA7n3LE"}]
    },
    "INTP": {
        "movies": [{"title": "매트릭스", "desc": "진리와 시스템의 본질을 탐구하는 철학자"},
                   {"title": "굿 윌 헌팅", "desc": "지적 호기심 가득한 천재 이야기"}],
        "music": [{"title": "Radiohead - Everything In Its Right Place", "url": "https://www.youtube.com/watch?v=onRk0sjSgFU"},
                  {"title": "Pink Floyd - Time", "url": "https://www.youtube.com/watch?v=JwYX52BP2Sk"}]
    },
    "ENTJ": {
        "movies": [{"title": "울프 오브 월 스트리트", "desc": "리더십과 추진력의 화신"},
                   {"title": "글래디에이터", "desc": "지휘관의 귀환"}],
        "music": [{"title": "Kanye West - POWER", "url": "https://www.youtube.com/watch?v=L53gjP-TtGE"},
                  {"title": "Imagine Dragons - Believer", "url": "https://www.youtube.com/watch?v=7wtfhZwyrcc"}]
    },
    "ENTP": {
        "movies": [{"title": "아이언맨", "desc": "발명가이자 유쾌한 천재"},
                   {"title": "소셜 네트워크", "desc": "혁신을 쫓는 야망가"}],
        "music": [{"title": "Gorillaz - Feel Good Inc.", "url": "https://www.youtube.com/watch?v=HyHNuVaZJ-k"},
                  {"title": "Queen - Don't Stop Me Now", "url": "https://www.youtube.com/watch?v=HgzGwKwLmgM"}]
    },
    "INFJ": {
        "movies": [{"title": "이터널 선샤인", "desc": "기억 너머의 감성을 품은 이야기"},
                   {"title": "어바웃 타임", "desc": "시간 속 진심을 찾는 여행"}],
        "music": [{"title": "Aurora - Runaway", "url": "https://www.youtube.com/watch?v=d_HlPboLRL8"},
                  {"title": "Sufjan Stevens - Mystery of Love", "url": "https://www.youtube.com/watch?v=KQT32vW61eI"}]
    },
    "INFP": {
        "movies": [{"title": "빅 피쉬", "desc": "상상과 현실의 경계를 넘나드는 따뜻한 이야기"},
                   {"title": "월플라워", "desc": "내성적인 감성의 성장기"}],
        "music": [{"title": "Bon Iver - Holocene", "url": "https://www.youtube.com/watch?v=TWcyIpul8OE"},
                  {"title": "Lana Del Rey - Video Games", "url": "https://www.youtube.com/watch?v=cE6wxDqdOV0"}]
    },
    "ENFJ": {
        "movies": [{"title": "데드 포엣 소사이어티", "desc": "가슴을 울리는 영감을 주는 이야기"},
                   {"title": "인턴", "desc": "세대와 소통, 그리고 진심"}],
        "music": [{"title": "Coldplay - Fix You", "url": "https://www.youtube.com/watch?v=k4V3Mo61fJM"},
                  {"title": "John Mayer - Gravity", "url": "https://www.youtube.com/watch?v=Fo4746vA44E"}]
    },
    "ENFP": {
        "movies": [{"title": "포레스트 검프", "desc": "열린 마음과 긍정의 아이콘"},
                   {"title": "업", "desc": "모험을 꿈꾸는 따뜻한 이야기"}],
        "music": [{"title": "Owl City - Fireflies", "url": "https://www.youtube.com/watch?v=psuRGfAaju4"},
                  {"title": "Jason Mraz - I'm Yours", "url": "https://www.youtube.com/watch?v=EkHTsc9PU2A"}]
    },
    "ISTJ": {
        "movies": [{"title": "캐치 미 이프 유 캔", "desc": "질서와 논리로 문제 해결"},
                   {"title": "본 아이덴티티", "desc": "기억과 정체성, 체계적인 추적"}],
        "music": [{"title": "The xx - Intro", "url": "https://www.youtube.com/watch?v=3gxNW2Ulpwk"},
                  {"title": "Daft Punk - Contact", "url": "https://www.youtube.com/watch?v=0Gkhol2Q1og"}]
    },
    "ISFJ": {
        "movies": [{"title": "센과 치히로의 행방불명", "desc": "정성과 보호 본능의 모험"},
                   {"title": "리틀 포레스트", "desc": "자연과 함께하는 정서적 치유"}],
        "music": [{"title": "Yiruma - River Flows in You", "url": "https://www.youtube.com/watch?v=7maJOI3QMu0"},
                  {"title": "IU - 밤편지", "url": "https://www.youtube.com/watch?v=BzYnNdJhZQw"}]
    },
    "ESTJ": {
        "movies": [{"title": "머니볼", "desc": "데이터 기반의 리더십"},
                   {"title": "설국열차", "desc": "체계 속에서의 결단력"}],
        "music": [{"title": "Muse - Uprising", "url": "https://www.youtube.com/watch?v=w8KQmps-Sog"},
                  {"title": "Eminem - Lose Yourself", "url": "https://www.youtube.com/watch?v=_Yhyp-_hX2s"}]
    },
    "ESFJ": {
        "movies": [{"title": "미 비포 유", "desc": "사랑과 돌봄의 이야기"},
                   {"title": "러브 액츄얼리", "desc": "모두를 위한 따뜻한 로맨스"}],
        "music": [{"title": "Bruno Mars - Just The Way You Are", "url": "https://www.youtube.com/watch?v=LjhCEhWiKXk"},
                  {"title": "Adele - Make You Feel My Love", "url": "https://www.youtube.com/watch?v=4-43lLKaqBQ"}]
    },
    "ISTP": {
        "movies": [{"title": "드라이브", "desc": "내면에 열정을 숨긴 조용한 해결사"},
                   {"title": "테넷", "desc": "과학과 행동의 조화"}],
        "music": [{"title": "Nirvana - Come As You Are", "url": "https://www.youtube.com/watch?v=vabnZ9-ex7o"},
                  {"title": "Linkin Park - Numb", "url": "https://www.youtube.com/watch?v=kXYiU_JCYtU"}]
    },
    "ISFP": {
        "movies": [{"title": "이터널스", "desc": "조용하지만 예술적인 감각"},
                   {"title": "아멜리에", "desc": "작은 선의가 만들어내는 따뜻한 변화"}],
        "music": [{"title": "Billie Eilish - Ocean Eyes", "url": "https://www.youtube.com/watch?v=viimfQi_pUw"},
                  {"title": "The Paper Kites - Bloom", "url": "https://www.youtube.com/watch?v=8inJtTG_DuU"}]
    },
    "ESTP": {
        "movies": [{"title": "분노의 질주", "desc": "액션과 속도의 인간"},
                   {"title": "킹스맨", "desc": "유쾌한 돌파력과 매너"}],
        "music": [{"title": "AC/DC - Thunderstruck", "url": "https://www.youtube.com/watch?v=v2AC41dglnM"},
                  {"title": "Pitbull - Fireball", "url": "https://www.youtube.com/watch?v=HMqgVXSvwGo"}]
    },
    "ESFP": {
        "movies": [{"title": "맘마미아!", "desc": "에너지 넘치는 무대 위 인생"},
                   {"title": "위대한 쇼맨", "desc": "무대와 환상의 세계"}],
        "music": [{"title": "Lady Gaga - Born This Way", "url": "https://www.youtube.com/watch?v=xtLX1nQZVPI"},
                  {"title": "Dua Lipa - Levitating", "url": "https://www.youtube.com/watch?v=TUVcZfQe-Kw"}]
    }
}

user_mbti = st.selectbox("당신의 MBTI를 선택하세요 👇", mbti_list)

if user_mbti:
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
        st.warning("이 MBTI에 대한 추천 정보가 없어요. 곧 추가할게요!")
