import streamlit as st
from final_24 import find_expression,format_expression

st.title("24点游戏解答")
st.info("输入四个1~10数字，点击“计算”按钮，即可得到一个可能的解答")
col1,col2,col3,col4=st.columns(4)
num1=col1.number_input("请输入第一个数字",min_value=1,max_value=10,value=1)
num2=col2.number_input("请输入第二个数字",min_value=1,max_value=10,value=5)
num3=col3.number_input("请输入第三个数字",min_value=1,max_value=10,value=5)
num4=col4.number_input("请输入第四个数字",min_value=1,max_value=10,value=5)
result=st.markdown(" ")
cal_button=st.button("计算")
if cal_button:
    nums=[num1,num2,num3,num4]
    steps, perm = find_expression(nums)
    if steps is not None:
        expression = format_expression(steps)
        result.markdown(f"找到可以得到 24 的计算式：\n{expression} = 24")
    else:
        result.markdown("无法通过四则运算得到 24。")
