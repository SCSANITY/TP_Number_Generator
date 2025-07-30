import streamlit as st
import datetime

st.set_page_config(page_title="TP_Number 線上生成器", page_icon="🧮", layout="centered")

st.title("📌 TP_Number 線上生成器")
st.markdown("請依照以下格式填寫，系統將自動生成 TP_Number。")

# 輸入欄位
surname = st.text_input("1. Surname（姓）", placeholder="如：Chen").strip().capitalize()
given_name = st.text_input("2. Given Name（名，空格分隔）", placeholder="如：Da Wen").strip()
birthday = st.text_input("3. Birthday（格式 YYYY-MM）", placeholder="2000-05").strip()
phone_last4 = st.text_input("4. Phone 後 4 碼", placeholder="如：1234").strip()

# 按鈕觸發
if st.button("🎯 生成 TP_Number"):
    if not surname or not given_name or not birthday or not phone_last4:
        st.error("請完整填寫所有欄位")
    else:
        try:
            birth_date = datetime.datetime.strptime(birthday, "%Y-%m")
            yymm = birth_date.strftime("%y%m")
        except:
            st.error("生日格式錯誤，請使用 YYYY-MM")
            st.stop()

        if not (phone_last4.isdigit() and len(phone_last4) == 4):
            st.error("電話後四位格式錯誤，必須是 4 位數字")
            st.stop()

        surname_fmt = surname[:4].ljust(4, "0")
        given_parts = given_name.split()

        first = given_parts[0][0].upper()
        second = given_parts[1][0].upper() if len(given_parts) > 1 else given_parts[0][1].lower()
        fn = (first + second).strip()

        tp_number = f"{surname_fmt}{fn}-{yymm}-{phone_last4}"
        st.success("✅ 生成成功！你的 TP_Number 為：")
        st.code(tp_number)
