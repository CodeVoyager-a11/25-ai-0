import streamlit as st

# 🎉 Streamlit 설정
st.set_page_config(page_title="MBTI 직업 추천기", page_icon="💼", layout="centered")

# 💖 제목
st.title("🌟 MBTI 기반 직업 추천기 🎯")
st.markdown("당신의 MBTI를 입력하면 어울리는 직업을 알려드려요! 💼✨")
st.markdown("대소문자 구분 없이 입력해보세요! (예: `infp`, `ENFP` 등) 😉")

with st.sidebar.expander("📋 MBTI 목록 리스트 보기"):
    mbti_descriptions = {
        "INFP": "이상주의적인 중재자 🌈",
        "ENFP": "열정적인 활동가 🔥",
        "INFJ": "통찰력 있는 조언자 🔮",
        "ENFJ": "타인을 이끄는 외교관 🤝",
        "INTP": "논리적인 사색가 🧠",
        "ENTP": "재치 있는 발명가 🛠️",
        "INTJ": "전략적인 계획자 🧩",
        "ENTJ": "카리스마 있는 리더 👑",
        "ISFJ": "성실한 수호자 🛡️",
        "ESFJ": "따뜻한 협력자 💗",
        "ISTJ": "책임감 있는 관리자 📋",
        "ESTJ": "체계적인 조직자 🏗️",
        "ISFP": "조용한 예술가 🎨",
        "ESFP": "자유로운 연예인 🎤",
        "ISTP": "실용적인 해결사 🔧",
        "ESTP": "모험적인 실행자 🏍️",
    }

    for mbti, desc in mbti_descriptions.items():
        st.markdown(f"🔹 **{mbti}** — {desc}")



# 🧠 MBTI - 직업 매칭 딕셔너리
mbti_jobs = {
    "INFP": ["작가 ✍️", "상담사 🧠", "그래픽 디자이너 🎨"],
    "ENFP": ["마케팅 전문가 📣", "창업가 🚀", "프로젝트 매니저 📋"],
    "INFJ": ["심리상담사 🧑‍⚕️", "작가 ✒️", "비영리단체 활동가 🌍"],
    "ENFJ": ["교사 👩‍🏫", "리더십 코치 🎤", "인사 담당자 🧑‍💼"],
    "INTP": ["연구원 🔬", "데이터 과학자 📊", "프로그래머 💻"],
    "ENTP": ["창업가 🚀", "기획자 📈", "마케팅 전략가 🧠"],
    "INTJ": ["전략 컨설턴트 📊", "엔지니어 ⚙️", "과학자 🔍"],
    "ENTJ": ["CEO 👑", "경영 컨설턴트 🧩", "프로젝트 리더 🧭"],
    "ISFJ": ["간호사 🩺", "초등학교 교사 🍎", "사회복지사 🤝"],
    "ESFJ": ["행정 직원 🏢", "이벤트 플래너 🎈", "간호조무사 💊"],
    "ISTJ": ["회계사 📚", "데이터 분석가 📈", "공무원 🏛️"],
    "ESTJ": ["팀 매니저 🧑‍💼", "운영 관리자 🏗️", "군인 🎖️"],
    "ISFP": ["패션 디자이너 👗", "사진작가 📸", "플로리스트 🌸"],
    "ESFP": ["연예인 🎤", "이벤트 코디네이터 🎉", "퍼포먼스 아티스트 💃"],
    "ISTP": ["기술자 🔧", "파일럿 🛩️", "응급 구조사 🚑"],
    "ESTP": ["세일즈 전문가 💼", "기업가 🏢", "스턴트 배우 🎬"]
}

# 🔽 드롭다운 입력창 (MBTI + 설명)
mbti_options = [f"{mbti} - {desc}" for mbti, desc in mbti_descriptions.items()]
selected = st.selectbox("🔍 MBTI를 선택하세요", options=mbti_options)

# 🔍 선택된 MBTI 코드 추출
selected_mbti = selected.split(" - ")[0]

# 🔎 추천 출력
st.subheader(f"✨ `{selected_mbti}` 유형의 설명")
st.info(f"{mbti_descriptions[selected_mbti]}")

st.subheader("💼 어울리는 직업 추천")
for job in mbti_jobs[selected_mbti]:
    st.success(f"✅ {job}")

# 📝 MBTI 입력 받기
user_mbti = st.text_input("당신의 MBTI를 입력해주세요 (예: INFP)", max_chars=4).upper()

if user_mbti:
    if user_mbti in mbti_jobs:
        st.subheader("✨ 어울리는 직업 추천:")
        for job in mbti_jobs[user_mbti]:
            st.success(f"✅ {job}")
        st.balloons()  # 🎈 풍선 효과
    else:
        st.error("❌ 유효한 MBTI 유형이 아닙니다. 다시 입력해주세요. (예: INFP, ENFP, ISTJ...)")

# 👣 푸터
st.markdown("---")
st.markdown("Made with  by someone")
