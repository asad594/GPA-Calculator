import streamlit as st
st.title("GPA Calculator")
course=st.number_input("How many Courses you have in your semester ")
total_points=0
total_credit=0
for i in range(1,int(course)+1):
    gpa=st.number_input(f"Enter the Gpa of course {i}")
    credit=st.number_input(f"Enter the credit hour of course {i}")
    total_points+=gpa*credit
    total_credit+=credit

if st.button("Calculate"):
    if total_credit > 0:
        final_Gpa=total_points/total_credit
        final=round(final_Gpa,3)
        st.success(f"The Gpa of semester is {final}")
    elif total_credit==0:
        st.error("Total credit hours cannot be zero.")

choice=st.text_input("Do you want to calculate the CGPA ? Yes or No")

if choice=="Yes":
    total_semester=st.number_input("Enter How many semester you passed")
    total_cgpa=0
    for i in range(1,int(total_semester+1)):
        cgpa=st.number_input(f"Enter the gpa of semester {i}")
        total_cgpa+=cgpa
    if st.button("Calculate CGPA"):
        if total_semester==0:
            st.error("Total semester cannot be zero.")
        else:
            final_cgpa=total_cgpa/total_semester
            st.success(f"The CGPA of {total_semester} semester is {final_cgpa}")
elif choice == "No":
    st.success("Thank You")
