# **Conversational Q&A Chatbot 🤖**

Welcome to the **Conversational Q&A Chatbot** repository! This project uses **gpt-4o-mini** to create an interactive chatbot that can answer your queries about Python or any programming language. 🌟

## **Overview**

This chatbot is built using **Streamlit** and **LangChain** to provide a seamless user experience. It allows users to input their questions and get responses from the **gpt-4o-mini** model. The UI is designed to be user-friendly and responsive, with custom CSS for styling.

## **Features**

- **Interactive Q&A**: Ask questions related to Python or any programming language.
- **Responsive UI**: Built with Streamlit, featuring custom CSS for enhanced user experience.
- **GPT-4o-mini**: Utilizes the gpt-4o-mini model for generating responses.

## **Installation**

To run this project locally, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/muhammadadilnaeem/Question-Answer-ChatBot-gpt-4o-mini.git
    cd Question-Answer-ChatBot-gpt-4o-mini
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:

    Create a `.env` file in the root directory and add your OpenAI API key:

    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

5. **Run the Streamlit app**:

    ```bash
    streamlit run app.py
    ```

## **Usage**

Once the app is running, you can open it in your browser at `http://localhost:8501`. Enter your questions in the input box and click "Submit" to get a response from the chatbot.

## **Code Explanation**

Here's a brief overview of the main components:

- **Imports**: Necessary libraries and modules are imported.
- **Environment Setup**: The OpenAI API key is loaded from the environment variables.
- **Streamlit UI**: The UI is set up using Streamlit's components, including custom CSS for styling.
- **Chat Model**: The `ChatOpenAI` model from `langchain_openai` is used to generate responses.
- **Response Handling**: User inputs are handled and responses are generated using the `invoke` method.

## **Contributing**

If you have suggestions or improvements, feel free to create a pull request or open an issue. Contributions are welcome!

## **License**

This project is licensed under the MIT License.

---

Happy coding! 💻
