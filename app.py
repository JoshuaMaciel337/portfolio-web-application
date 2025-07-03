from flask import Flask, render_template

app = Flask(__name__)

# Sample dynamic data for portfolio projects and other sections
portfolio_projects = [
    {
        "title": "Mobile Applications",
        "image": "https://wdtworkz.wpengine.com/wp-content/uploads/2025/05/Smartphone-Apps.jpg",
        "description": "Show More"
    },
    {
        "title": "Branding Creation",
        "image": "https://wdtworkz.wpengine.com/wp-content/uploads/2025/05/Branding-Design.jpg",
        "description": "Show More"
    },
    {
        "title": "Creative Layout",
        "image": "https://wdtworkz.wpengine.com/wp-content/uploads/2025/05/Creative-Template.jpg",
        "description": "Show More"
    },
    {
        "title": "Artistic Visuals",
        "image": "https://wdtworkz.wpengine.com/wp-content/uploads/2025/05/Visual-Arts.jpg",
        "description": "Show More"
    },
    {
        "title": "Identifier",
        "image": "https://wdtworkz.wpengine.com/wp-content/uploads/2025/05/Trademark.jpg",
        "description": "Show More"
    },
    {
        "title": "Mobile Software",
        "image": "https://wdtworkz.wpengine.com/wp-content/uploads/2025/05/Smartphone-Apps.jpg",
        "description": "Show More"
    },
    {
        "title": "Brand Styling",
        "image": "https://wdtworkz.wpengine.com/wp-content/uploads/2025/05/Branding-Design.jpg",
        "description": "Show More"
    }
]

@app.route('/')
def index():
    return render_template('index.html', projects=portfolio_projects)

if __name__ == '__main__':
    app.run(debug=True)
