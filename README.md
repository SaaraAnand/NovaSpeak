\documentclass{article}
\usepackage{hyperref}
\usepackage{graphicx}

\title{\textbf{🎤 NovaSpeak: Your Personal AI Voice Assistant}}
\author{Developed by: Saara and Neelmani}
\date{}

\begin{document}

\maketitle

\section{Introduction}
NovaSpeak is an AI-powered voice assistant built using \textbf{Streamlit, SpeechRecognition, Pyttsx3, and LangChain}. It leverages the \textbf{Mistral} language model via Ollama to facilitate human-like conversations, transcribing speech to text and responding in real time. The application features a sleek user interface with custom styling and provides interactive AI-powered responses.

\begin{figure}[h]
    \centering
    \includegraphics[width=0.8\textwidth]{live_model.png} % Replace with actual image filename
    \caption{Live Demo of NovaSpeak AI Assistant}
\end{figure}

\section{Features}
\begin{itemize}
    \item 🎙 Speech-to-text recognition using Google Speech API.
    \item 🤖 AI-driven responses powered by the \textbf{Mistral} LLM from Ollama.
    \item 🔊 Text-to-speech conversion for AI responses.
    \item 📜 Interactive chat history stored using LangChain.
    \item 🎨 Custom styled UI using Streamlit markdown and CSS.
\end{itemize}

\section{Installation}
To set up and run NovaSpeak, follow these steps:

\subsection{Prerequisites}
Ensure you have \textbf{Python 3.8+} installed. Also, install \textbf{Ollama} from:  
\url{https://ollama.ai/download}

\subsection{Clone the Repository}
\begin{verbatim}
git clone https://github.com/your-repo/NovaSpeak.git
cd NovaSpeak
\end{verbatim}

\subsection{Install Dependencies}
Install required Python libraries using:
\begin{verbatim}
pip install -r requirements.txt
\end{verbatim}

\subsection{Run the Application}
To start the application, run:
\begin{verbatim}
streamlit run app.py
\end{verbatim}
This will launch the web UI in your browser.

\section{Requirements.txt}
\begin{verbatim}
streamlit
speechrecognition
pyttsx3
langchain
langchain-community
langchain-core
ollama
matplotlib
seaborn
\end{verbatim}

\section{Usage}
\begin{enumerate}
    \item Click the \textbf{🎙 Start Listening} button.
    \item Speak into your microphone.
    \item The AI will transcribe your speech and generate a response.
    \item The response will be displayed on the screen and spoken aloud.
    \item View the full chat history at the bottom of the page.
\end{enumerate}

\section{Contributors}
\begin{itemize}
    \item \textbf{Saara}
    \item \textbf{Neelmani Ramkripalu}
\end{itemize}

\section{License}
This project is open-source and available under the MIT License.

\end{document}
