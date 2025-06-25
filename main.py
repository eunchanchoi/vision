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
recommendations = {
    "INTJ": {
        "movies": [
            {"title": "인셉션", "desc": "복잡한 구조 속에서도 통제하려는 전략가"},
            {"title": "셜록", "desc": "논리와 추리의 끝판왕"}
        ],
        "music": [
            {"title": "Hans Zimmer - Time", "url": "https://www.youtube.com/watch?v=RxabLA7UQ9k"},
            {"title": "Ludovico Einaudi - Experience", "url": "https://www.youtube.com/watch?v=91pFNA7n3LE"}
        ]
    },
    "INTP": {
        "movies": [
            {"title": "매트릭스", "desc": "진리와 시스템의 본질을 탐구하는 철학자"},
            {"title": "굿 윌 헌팅", "desc": "지적 호기심 가득한 천재 이야기"}
        ],
        "music": [
            {"title": "Radiohead - Everything In Its Right Place", "url": "https://www.youtube.com/watch?v=onRk0sjSgFU"},
            {"title": "Pink Floyd - Time", "url": "https://www.youtube.com/watch?v=JwYX52BP2Sk"}
        ]
    },
    "ENTJ": {
        "movies": [
            {"title": "울프 오브 월 스트리트", "desc": "리더십과 추진력의 화신"},
            {"title": "글래디에이터", "desc": "지휘관의 귀환"}
        ],
        "music": [
            {"title": "Kanye West - POWER", "url": "https://www.youtube.com/watch?v=L53gjP-TtGE"},
            {"title": "Imagine Dragons - Believer", "url": "https://www.youtube.com/watch?v=7wtfhZwyrcc"}
        ]
    },
    "ENTP": {
        "movies": [
            {"title": "아이언맨", "desc": "발명가이자 유쾌한 천재"},
            {"title": "소셜 네트워크", "desc": "혁신을 쫓는 야망가"}
        ],
        "music": [
            {"title": "Gorillaz - Feel Good Inc.", "url": "https://www.youtube.com/watch?v=HyHNuVaZJ-k"},
            {"title": "Queen - Don't Stop Me Now", "url": "https://www.youtube.com/watch?v=HgzGwKwLmgM"}
        ]
    },
    "INFJ": {
        "movies": [
            {"title": "어바웃 타임", "desc": "삶의 의미를 음미하는 이상주의자"},
            {"title": "이터널 선샤인", "desc": "기억과 감정의 여운"}
        ],
        "music": [
            {"title": "Sigur Rós - Hoppípolla", "url": "https://www.youtube.com/watch?v=DiU8Jb2JQEc"},
            {"title": "Lana Del Rey - Young and Beautiful", "url": "https://www.youtube.com/watch?v=o_1aF54DO60"}
        ]
    },
    "INFP": {
        "movies": [
            {"title": "빅 피쉬", "desc": "상상과 감성이 살아있는 이야기꾼"},
            {"title": "월플라워", "desc": "내면의 성장과 따뜻한 우정"}
        ],
        "music": [
            {"title": "Aurora - Runaway", "url": "https://www.youtube.com/watch?v=d_HlPboLRL8"},
            {"title": "Sufjan Stevens - Mystery of Love", "url": "https://www.youtube.com/watch?v=KQT32vW61eI"}
        ]
    },
    "ENFJ": {
        "movies": [
            {"title": "죽은 시인의 사회", "desc": "영감을 주는 지도자"},
            {"title": "히든 피겨스", "desc": "사람을 위한 변화의 주체"}
        ],
        "music": [
            {"title": "Alicia Keys - Girl on Fire", "url": "https://www.youtube.com/watch?v=J91ti_MpdHA"},
            {"title": "U2 - Beautiful Day", "url": "https://www.youtube.com/watch?v=co6WMzDOh1o"}
        ]
    },
    "ENFP": {
        "movies": [
            {"title": "월터의 상상은 현실이 된다", "desc": "모험을 향한 설렘"},
            {"title": "라라랜드", "desc": "꿈과 열정이 춤추는 이야기"}
        ],
        "music": [
            {"title": "Coldplay - Adventure of a Lifetime", "url": "https://www.youtube.com/watch?v=QtXby3twMmI"},
            {"title": "BTS - Dynamite", "url": "https://www.youtube.com/watch?v=gdZLi9oWNZg"}
        ]
    },
    "ISTJ": {
        "movies": [
            {"title": "스포트라이트", "desc": "원칙을 따르는 진실 탐구"},
            {"title": "브릿지 오브 스파이", "desc": "정직함과 신념의 균형"}
        ],
        "music": [
            {"title": "Beethoven - Symphony No. 5", "url": "https://www.youtube.com/watch?v=fOk8Tm815lE"},
            {"title": "The Beatles - Let It Be", "url": "https://www.youtube.com/watch?v=QDYfEBY9NM4"}
        ]
    },
    "ISFJ": {
        "movies": [
            {"title": "인턴", "desc": "헌신과 배려가 만들어내는 따뜻함"},
            {"title": "작은 아씨들", "desc": "가족과 전통을 중시하는 이야기"}
        ],
        "music": [
            {"title": "Norah Jones - Don't Know Why", "url": "https://www.youtube.com/watch?v=tO4dxvguQDk"},
            {"title": "John Mayer - Gravity", "url": "https://www.youtube.com/watch?v=Fo4746nq76o"}
        ]
    },
    "ESTJ": {
        "movies": [
            {"title": "머니볼", "desc": "실용성과 전략으로 이끄는 리더"},
            {"title": "다크 나이트", "desc": "질서를 지키는 정의감"}
        ],
        "music": [
            {"title": "Survivor - Eye of the Tiger", "url": "https://www.youtube.com/watch?v=btPJPFnesV4"},
            {"title": "Muse - Uprising", "url": "https://www.youtube.com/watch?v=w8KQmps-Sog"}
        ]
    },
    "ESFJ": {
        "movies": [
            {"title": "코코", "desc": "가족과 전통을 소중히 여기는 마음"},
            {"title": "업", "desc": "정감 있는 관계와 헌신"}
        ],
        "music": [
            {"title": "Jason Mraz - I'm Yours", "url": "https://www.youtube.com/watch?v=EkHTsc9PU2A"},
            {"title": "Kelly Clarkson - Stronger", "url": "https://www.youtube.com/watch?v=Xn676-fLq7I"}
        ]
    },
    "ISTP": {
        "movies": [
            {"title": "본 아이덴티티", "desc": "신중하면서도 효율적인 문제 해결자"},
            {"title": "매드맥스: 분노의 도로", "desc": "감각과 반응이 살아있는 액션"}
        ],
        "music": [
            {"title": "The White Stripes - Seven Nation Army", "url": "https://www.youtube.com/watch?v=0J2QdDbelmY"},
            {"title": "Arctic Monkeys - Do I Wanna Know?", "url": "https://www.youtube.com/watch?v=bpOSxM0rNPM"}
        ]
    },
    "ISFP": {
        "movies": [
            {"title": "비긴 어게인", "desc": "감성적인 아티스트의 여정"},
            {"title": "원스", "desc": "음악으로 이어지는 감정"}
        ],
        "music": [
            {"title": "Ed Sheeran - Photograph", "url": "https://www.youtube.com/watch?v=nSDgHBxUbVQ"},
            {"title": "Billie Eilish - Ocean Eyes", "url": "https://www.youtube.com/watch?v=viimfQi_pUw"}
        ]
    },
    "ESTP": {
        "movies": [
            {"title": "베이비 드라이버", "desc": "스피드와 감각의 쾌감"},
            {"title": "킹스맨", "desc": "스타일과 액션의 정석"}
        ],
        "music": [
            {"title": "The Weeknd - Blinding Lights", "url": "https://www.youtube.com/watch?v=4NRXx6U8ABQ"},
            {"title": "David Guetta - Titanium", "url": "https://www.youtube.com/watch?v=JRfuAukYTKg"}
        ]
    },
    "ESFP": {
        "movies": [
            {"title": "맘마미아!", "desc": "에너지 넘치는 무대 위 인생"},
            {"title": "위대한 쇼맨", "desc": "무대와 환상의 세계"}
        ],
        "music": [
            {"title": "Lady Gaga - Born This Way", "url": "https://www.youtube.com/watch?v=xtLX1nQZVPI"},
            {"title": "Dua Lipa - Levitating", "url": "https://www.youtube.com/watch?v=TUVcZfQe-Kw"}
        ]
    }
}

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

