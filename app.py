from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Mock user data (username: password)
users = {
    'user': 'password'
}

# In-memory debate storage
debates = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'danger')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', debates=debates)
    else:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))

@app.route('/create-debate', methods=['GET', 'POST'])
def create_debate():
    if request.method == 'POST':
        title = request.form['topic']  # Update to match form field
        description = request.form['description']
        date = request.form['date']  # Capture the date if needed

        # Save the debate to the list
        debates.append({'title': title, 'description': description, 'date': date})
        flash('Debate created successfully!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('create_debate.html')
@app.route('/debate1.html')
def debate1():
    return render_template('debate1.html')

@app.route('/debate2.html')
def debate2():
    return render_template('debate2.html')

@app.route('/debate3.html')
def debate3():
    return render_template('debate3.html')

@app.route('/debate4.html')
def debate4():
    return render_template('debate4.html')

@app.route('/debate5.html')
def debate5():
    return render_template('debate5.html')

@app.route('/debate6.html')
def debate6():
    return render_template('debate6.html')

@app.route('/debate7.html')
def debate7():
    return render_template('debate7.html')

@app.route('/debate8.html')
def debate8():
    return render_template('debate8.html')







# In-memory debate storage
debates = []

# Pre-populate a debate for testing
debates.append({
    'title': 'Should Vaccination Be Mandatory?',
    'description': 'The debate on whether vaccination should be mandatory centers around public health and individual rights. Proponents argue that mandatory vaccination is essential for achieving herd immunity, protecting vulnerable populations who cannot be vaccinated, and preventing outbreaks of diseases like measles and polio, which have been largely controlled through vaccination efforts. They emphasize that vaccines save millions of lives each year and that existing mandates for school enrollments demonstrate their effectiveness in maintaining high vaccination rates. In contrast, opponents contend that making vaccination mandatory infringes on personal autonomy and individual rights, advocating for informed choice instead. They highlight concerns about vaccine safety and the potential for mistrust in medical authorities if people feel coerced. Ultimately, the debate raises crucial questions about balancing public health imperatives with respect for individual freedoms.',
    'date': '2024-10-29'
})

@app.route('/debate/<int:debate_id>')
def debate(debate_id):
    if 0 <= debate_id < len(debates):
        debate = debates[debate_id]
        return render_template('debate.html', debate=debate)
    else:
        flash('Debate not found.', 'danger')
        return redirect(url_for('dashboard'))
    

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('login'))

@app.route('/my-debates')
def my_debates():
    return render_template('my-debates.html', debates=debates)

if __name__ == '__main__':
    app.run(debug=True)

