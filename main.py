import streamlit as st

# 🎉 Streamlit 설정
st.set_page_config(page_title="MBTI 직업 추천기", page_icon="💼", layout="centered")

# 💖 제목
st.title("🌟 MBTI 기반 직업 추천기 🎯")
st.markdown("당신의 MBTI를 입력하면 어울리는 직업을 알려드려요! 💼✨")

# 🧠 MBTI - 직업 매칭 딕셔너리
mbti_jobs = {
    "INFP": ["작가 ✍️", "상담사 🧠", "디자이너 🎨"],
    "ENFP": ["마케팅 전문가 📣", "스타트업 창업자 🚀", "기획자 📋"],
    "ISTJ": ["회계사 🧾", "데이터 분석가 📊", "행정가 🏢"],
    "ENTJ": ["CEO 👑", "전략 컨설턴트 🧩", "경영자 📈"],
    # 필요시 더 추가 가능
}

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
st.markdown("Made with ❤️ by ChatGPT")
