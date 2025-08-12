# -Build-a-Portfolio-Website-with-Flask
 # 💼 Task 6: Build a Portfolio Website with Flask

## 📌 Objective

Create a personal portfolio website using **Flask** that showcases your skills, projects, certifications, goals, and includes a working contact form. This task demonstrates your ability to build a real-world mini web app with backend integration.

## 🧰 Tools Used

- **Python** – Programming language
- **Flask** – Lightweight web framework
- **HTML & CSS** – Frontend structure and styling

## ⚙️ How to Install Tools

Make sure Python is installed. Then install Flask:

``bash :- pip install flask

## 📁 Files Included

portfolio/ 
├── app.py # Flask application with routing and form handling 
├── index.html # Main HTML page with embedded CSS and contact form 
├── messages.txt # Auto-generated file storing submitted messages

🚀 How to Run the Project
Open terminal in the portfolio/ folder.
Run the Flask app:
bash :- python app.py
Open your browser and visit:-http://localhost:5000

🗄️ Sample Output (Text-Based)
Contact Form Submission:
Visitor fills out:
Name: Shaik
Email: shaik@example.com
Message: Interested in collaborating!

Terminal Output:
Message from Shaik (shaik@example.com): Interested in collaborating!
File Output (messages.txt):
Shaik | shaik@example.com | Interested in collaborating!
Browser Popup:
✅ Message sent successfully!

📊 Insights
Flask routing (/ and /contact) is used to serve the page and handle form submissions.
Contact form data is saved locally in messages.txt for simplicity.
Popup alert confirms successful submission, enhancing user experience.
All content is embedded in a single HTML file for minimal setup.

🏁 Outcome
✅ A fully functional portfolio website with:
Skills, projects, certifications, and goals
A working contact form with backend logic
Message persistence using .txt file
Clean UI and responsive layout

