from preprocess_text import preprocess_text
from db_setup import create_connection, create_table, insert_response, fetch_response

def chatbot():
    database = "chatbot.db"
    conn = create_connection(database)
    create_table(conn)
    
    print("Hello! I am your chatbot. How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        processed_input = preprocess_text(user_input)
        response = fetch_response(conn, ' '.join(processed_input))
        
        if response:
            print("Bot:", response)
        else:
            if 'add' in processed_input:
                try:
                    insert_response(conn, ' '.join(processed_input), user_input)
                    print("Bot: Got it! I've added that to my memory.")
                except Exception as e:
                    print("Bot: Oops! I couldn't add that to my memory.")
            else:
                print("Bot: I'm working on that. Please specify what you'd like me to do.")
    
    if conn:
        conn.close()

if __name__ == '__main__':
    chatbot()
