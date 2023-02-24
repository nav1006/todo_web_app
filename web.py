import streamlit as st
import functionsTODO as fn

todos = fn.get_todos()

def add_todo():
        todo = st.session_state['new_todo'] + "\n"
        todos.append(todo)
        fn.write_todos(todos)


st.title('TO-DO App')
st.write('This app will help you to keep track of your activities.')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fn.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder='Add new todo...',
              on_change= add_todo, key='new_todo')
