from flask import Flask, render_template

app = Flask(__name__)

# Route for Home (CV/Resume page)
@app.route('/')
def index():
    return render_template('index.html')

# Route for Projects section
@app.route('/projects')
def projects():
    return render_template('projects.html')

# Route for Blogs section
@app.route('/blogs')
def blogs():
    return render_template('blogs.html')

# Route for Contact section
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
