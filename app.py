from flask import Flask, request, render_template_string

app = Flask(__name__)

# Load your HTML content from index.html
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

@app.route('/')
def home():
    return render_template_string(html_content)

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    with open("messages.txt", "a", encoding="utf-8") as f:
        f.write(f"{name} | {email} | {message}\n")

    success_script = """
    <script>
      alert("✅ Message sent successfully!");
    </script>
    """

    return render_template_string(html_content + success_script)

if __name__ == '__main__':
    app.run(debug=True)
