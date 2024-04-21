import streamlit as st
def main():
  st.title("Find The Largest Number")
  num1 = st.number_input("Enter the first number:", step=1)
  num2 = st.number_input("Enter the second number:", step=1)
  num3 = st.number_input("Enter the third number:", step=1)
  if st.button("Find The Largest"):
    largest = max(num1,num2,num3)
    st.write("The Largest Number is: ",largest)
if __name__ == "__main__":
  main()

