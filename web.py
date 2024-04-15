import streamlit as st
from functions import get_todos, write_todos

todos = get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    write_todos(todos)

st.title('My TODO App')
st.subheader('Welcome to the To-Do App.')
st.write('This app is to increase your productivity by helping you keep track of your tasks.')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)

    if checkbox:
        todos.pop(index)
        write_todos(todos)

        del st.session_state[todo]
        st.rerun()

st.text_input(label='', placeholder='Enter a new TODO',
              on_change=add_todo, key='new_todo')


