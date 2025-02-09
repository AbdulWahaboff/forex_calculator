import streamlit as st

# Custom header with logo and title
col1, col2 = st.columns([1, 3])  # Create two columns

# Display logo on the left
with col1:
    st.image("logo.PNG", width=120)  # Adjust width as needed

# Display "Trading Hub Academy" on the right
with col2:
    st.markdown(
        """
        <h1 style="text-align: centre; color: #007BFF;">Trading Hub Academy</h1>
        """,
        unsafe_allow_html=True,
    )

def calculate_sl_tp(account_balance, risk_percentage, entry_price, lot_size, rr_ratio):
    try:
        risk_amount = (account_balance * risk_percentage) / 100
        pip_value = (lot_size / 0.01) * 1  # Adjust as needed
        sl_pips = risk_amount / pip_value
        stop_loss = entry_price - sl_pips
        
        reward_ratio = int(rr_ratio.split(':')[1])
        tp_pips = sl_pips * reward_ratio
        take_profit = entry_price + tp_pips
        target_profit_amount = risk_amount * reward_ratio

        return stop_loss, take_profit, risk_amount, target_profit_amount
    
    except Exception as e:
        return None, None, None, None

st.title("💰 Forex SL & TP Calculator")

account_balance = st.number_input("💵 Account Size ($)", min_value=0.0)
risk_percentage = st.number_input("📊 Risk Percentage (%)", min_value=0.0, max_value=100.0)
entry_price = st.number_input("📈 Entry Price", min_value=0.0)
lot_size = st.number_input("📊 Lot Size", min_value=0.01)
rr_ratio = st.selectbox("📉 Risk to Reward Ratio", ["1:2", "1:3", "1:4"])

if st.button("Calculate SL & TP"):
    stop_loss, take_profit, risk_amount, target_profit_amount = calculate_sl_tp(account_balance, risk_percentage, entry_price, lot_size, rr_ratio)

    if stop_loss and take_profit:
        st.success(f"🔴 Stop Loss: {stop_loss:.2f}")
        st.success(f"🟢 Take Profit: {take_profit:.2f}")
        st.info(f"⚠️ You are risking **${risk_amount:.2f}** to gain **${target_profit_amount:.2f}**")
    else:
        st.error("❌ Invalid input values. Please check your entries.")
