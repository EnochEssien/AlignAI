import subprocess
import tempfile
import os
import shutil

def latex_to_pdf(latex_code, output_pdf_name="output.pdf", output_dir="."):
    # Create a temporary working directory
    with tempfile.TemporaryDirectory() as tmpdir:
        tex_path = os.path.join(tmpdir, "document.tex")

        # Write LaTeX code to temporary .tex file
        with open(tex_path, "w", encoding="utf-8") as f:
            f.write(latex_code)

        try:
            # Compile LaTeX to PDF using pdflatex
            subprocess.run(
                ['pdflatex', '-interaction=nonstopmode', 'document.tex'],
                cwd=tmpdir,
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            # Move PDF to the desired location with the given name
            pdf_path = os.path.join(tmpdir, "document.pdf")
            final_path = os.path.join(output_dir, output_pdf_name)
            shutil.move(pdf_path, final_path)

            print(f"✅ PDF successfully created at: {final_path}")
        except subprocess.CalledProcessError as e:
            print("❌ LaTeX compilation failed.")
            print(e)

# Example LaTeX content (can be anything you want)
latex_code = r"""
\documentclass[a4paper,10pt]{article}
\usepackage{enumitem}
\usepackage{geometry}
\usepackage{hyperref}
\usepackage{titlesec}
\usepackage{parskip}
\geometry{margin=1in}

\titleformat{\section}{\normalfont\Large\bfseries}{\thesection}{1em}{}
\titleformat{\subsection}{\normalfont\large\bfseries}{\thesubsection}{1em}{}

\begin{document}

\begin{center}
    \textbf{\Huge Enoch NM Essien} \\
    27 Muller Street North, Buccleuch, Johannesburg, 2090, South Africa \\
    +27 63 155 2047 | \href{mailto:enochessien05@gmail.com}{enochessien05@gmail.com}\\
    \href{https://enochessien.netlify.app/}{https://enochessien.netlify.app/}
\end{center}

\section*{}
\noindent
A diligent, adaptable, and results-driven individual with a strong work ethic and excellent interpersonal skills. My journey began with a deep passion for robotics, but over time, my ambitions have evolved into the AI space. As a natural problem solver, my aim is to take advantage of this ability to address real-world challenges. My experiences have equipped me not only with technical skills but also with the ability to work effectively with diverse teams and drive impactful projects.

\section*{EDUCATION}
\noindent
\textbf{The University of Johannesburg, South Africa} \\
Masters of Artificial Intelligence and Machine Learning\\
\textit{Expected March 2025} \\
Relevant modules: Introduction to Programming for AI, Natural Language Processing, Machine learning, Ethics of AI, Mathematics and Statistics for AI.

\noindent
\textbf{The University of the West of England, Bristol, United Kingdom} \\
Bachelor of Engineering in Robotics Engineering \\
\textit{August 2021} \\
Relevant modules: C programming, Practical Electronic and Electronic design, Introductory artificial intelligence, Bio computation and Intelligent Adaptive systems, Advanced Machine Vision.

\section*{SKILLS}
\noindent
\textbf{Software Programming:} \\
Proficient in various programming languages including C, Python, Java, MATLAB, and R. \\
Experience gained through degree coursework, personal projects, and advanced online courses.

\noindent
\textbf{Machine Learning:} \\
Applied programming techniques associated with Artificial Intelligence, including genetic algorithms for optimization, neural networks, deep learning, supervised/unsupervised learning, and reinforcement learning. \\
Extensive knowledge in machine vision, constructing algorithms to identify features in images, expanding understanding of AI applications in robotics. \\
Familiar with machine learning frameworks such as TensorFlow, PyTorch, Numpy, Pandas, and Scikit-Learn.

\noindent
\textbf{Web Development:} \\
Trained in Full Stack web development through online courses. \\
Proficient in frontend languages and libraries such as HTML5, CSS3, Bootstrap4. \\
Experience with backend development using PHP and SQL, and building dynamic web applications with React.js and JavaScript ES6.

\noindent
\textbf{LaTeX:} \\
Proficient in document preparation and academic writing using LaTeX for formal reports, CVs, and research papers.

\newpage
 
\section*{WORK EXPERIENCE}
\noindent
\textbf{Head of Operations | Innovation Lab, Johannesburg Business School, South Africa} \\
\textit{January 2024 – Present} \\
\begin{itemize}[leftmargin=0.5cm]
    \item Lead and manage the daily operations of the Innovation Lab, a software development unit within the University of Johannesburg.
    \item Aid in strategic decision-making for projects related to AI tools and digital solutions for businesses.
    \item Collaborate with cross-functional teams to develop software solutions and optimize business processes.
\end{itemize}

\noindent
\textbf{GLA Bootcamp Coordinator | GRIT Lab Africa, South Africa} \\
\textit{August 2024 – November 2024} \\
\begin{itemize}[leftmargin=0.5cm]
    \item Led a coding bootcamp for 500+ students, equipping them with industry-relevant programming skills.
    \item Designed and delivered structured learning content, improving student engagement and retention.
    \item Provided technical mentorship, resulting in a 70\%+ graduation rate, demonstrating the program's effectiveness.
\end{itemize}

\noindent
\textbf{Coordinator | Digital Innovation and AI Tools for Small Businesses Program, Johannesburg Business School, South Africa} \\
\textit{January 2024 – March 2024} \\
\begin{itemize}[leftmargin=0.5cm]
    \item Designed and delivered AI and digital innovation training for 70+ small business owners, enhancing their digital capabilities
    \item Enabled businesses to adopt AI-driven solutions, leading to operational efficiency and improved market competitiveness.
    \item Provided hands-on guidance in integrating AI tools, contributing to a 60\%+ graduation rate and measurable business growth.
\end{itemize}

\noindent
\textbf{Research Assistant | GRIT Lab Africa, Johannesburg Business School, South Africa} \\
\textit{October 2023 – January 2024} \\
\begin{itemize}[leftmargin=0.5cm]
    \item Conducted data-driven research on entrepreneurship and sustainable development, contributing to actionable business strategies.
    \item Assisted in data collection and analysis, leading to impactful research publications.
    \item Developed and tested AI-based business solutions, enhancing economic opportunities in African markets.
\end{itemize}

\noindent
\textbf{Independent Machine Learning Consultant | Annuo Medical Technology Solutions, Australia} \\
\textit{January 2022 – July 2022} \\
\begin{itemize}[leftmargin=0.5cm]
    \item Consulted on machine learning applications in healthcare, guiding AI model selection for medical diagnostics
    \item Contributed to algorithm development, improving the accuracy and efficiency of patient care solutions.
\end{itemize}

\noindent
\textbf{Full-Stack Web Developer | PathUp Africa, Lagos, Nigeria} \\
\textit{October 2021 – May 2022} \\
\begin{itemize}[leftmargin=0.5cm]
    \item Led the design and deployment of a dynamic web platform, optimizing user experience and accessibility.
    \item Utilized HTML5, CSS3, Bootstrap4, JavaScript (ES6), jQuery, PHP, and SQL to build scalable solutions.
    \item Delivered a functional, responsive website that enhanced the organization’s digital presence and engagement.
\end{itemize}


\section*{PROJECTS - \href{https://enochessien.netlify.app/}{https://enochessien.netlify.app/}}
\noindent
\textbf{Undergraduate Final Dissertation Project: Monocular Visual SLAM for Mobile Robots} \\
\textit{September 2020 – July 2021} \\
\begin{itemize}[leftmargin=0.5cm]
    \item Applied Monocular Visual SLAM techniques on a commercial microcomputer in a mobile robot to remotely control and map its surroundings.
    \item The project aimed to create more advanced robotic applications while reducing the cost of training robots using regular cameras instead of high-spec sensors such as LIDAR.
    \item Implemented skills acquired during my robotics course and extended beyond to study other robotics techniques, including using ROS.
\end{itemize}

\noindent
\textbf{Application of a Siamese Neural Network for One-Shot Facial Recognition (Research Paper for Master's)} \\
\textit{August 2024 – Present} \\
\begin{itemize}[leftmargin=0.5cm]
    \item Developed a facial recognition system using a Siamese Neural Network for one-shot learning to differentiate individuals from limited image samples.
    \item This research paper is planned to be submitted before the end of my Master's program in 2024, with future improvements integrating additional facial features for higher accuracy.
\end{itemize}

\noindent
\textbf{AfriMaths Tutor: AI-Enhanced Learning Tools and Synthetic Data Generation for IsiZulu Mathematics (Research Project for Master's)} \\
\textit{January 2024 – Present} \\
\begin{itemize}[leftmargin=0.5cm]
    \item Designed a rule-based algorithm to synthesize linear equation problems and solutions in isiZulu, addressing the challenge of mathematics anxiety among Grade 10 students in South Africa.
    \item Developed an Intelligent Tutoring System (ITS) using AI to deliver culturally and linguistically sensitive education.
    \item Focuses on evaluating the effectiveness of AI-driven tutoring and its impact on mathematics performance in local African languages.
\end{itemize}

\noindent
\textbf{Automatic Extraction of Tone for Sesotho (Research Project for Master's)} \\
\textit{August 2024 – Present} \\
\begin{itemize}[leftmargin=0.5cm]
    \item Developed a system for the automatic extraction of tone for Sesotho, a crucial phonetic feature in many African languages, to enhance NLP applications like speech recognition and language learning tools.
    \item Focuses on accurately identifying pitch contours in Sesotho speech and mapping them to the appropriate tone categories.
\end{itemize}

\noindent
\textbf{Dreamathon VR Project: Anansi (Hackathon, July 2024)} \\
\textit{July 2024} \\
\begin{itemize}[leftmargin=0.5cm]
    \item Participated in the Dreamathon coordinated by the Computational Design Institute (CDI) Program, where my team developed a VR concept called "Anansi."
    \item Anansi is a virtual reality game based on African folktales, designed to aid in palliative care and stress reduction.
    \item My team won recognition and prize money for our innovative VR solution.
\end{itemize}

\noindent
\textbf{Other Personal Projects} \\
\textit{December 2020 – Present} \\
\begin{itemize}[leftmargin=0.5cm]
    \item Trained and deployed object detectors and image classifiers using machine learning, computer vision, and TensorFlow.
    \item Developed a custom-trained Face Mask Detector using the TensorFlow object detection API.
    \item Created a Convolutional Neural Network trained on the CIFAR-10 dataset, achieving 85\% accuracy.
    \item Developed a custom-trained object detector for identifying human individuals in images.
    \item Implemented a Genetic Algorithm in Python to solve various minimization functions.
\end{itemize}

\section*{CERTIFICATIONS}
\noindent
\textbf{Nvidia Fundamentals of Deep Learning} \\
Nvidia | \textit{September 2024} \\
Learned foundational deep learning techniques, including neural networks, optimization methods, and AI applications.

\noindent
\textbf{Deep Learning and Computer Vision A-Z} \\
Udemy | \textit{December 14, 2021} \\
Developed expertise in deep learning and computer vision techniques, including neural networks and image recognition.

\noindent
\textbf{The Complete Web Development Bootcamp} \\
Udemy | \textit{December 20, 2021} \\
Proficient in front-end and back-end web development, creating responsive and dynamic websites and web applications.

\noindent
\textbf{Machine Learning A-Z: Python} \\
Udemy | \textit{December 28, 2021} \\
Acquired in-depth knowledge of machine learning algorithms and their applications in Python.

\noindent
\textbf{Complete Python Developer in 2022: Zero to Mastery} \\
Udemy | \textit{January 5, 2022} \\
Mastered Python programming for various applications, including web development, automation, and data analysis.

\noindent
\textbf{CS50's Introduction to Computer Science} \\
Harvard University | \textit{December 2023} \\
Gained foundational knowledge in computer science, including problem-solving and algorithmic thinking.

\noindent
\textbf{CS50's Introduction to Artificial Intelligence} \\
Harvard University | \textit{December 2023} \\
Explored the fundamentals of artificial intelligence and machine learning techniques.

\end{document}

"""

# Run it
if __name__ == "__main__":
    latex_to_pdf(latex_code, output_pdf_name="final_output.pdf")
