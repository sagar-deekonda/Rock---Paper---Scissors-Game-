from flask import Flask, render_template, request
import numpy as np

User_Score = 0
Computer_Score = 0

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/play", methods=["POST"])
def play():

    global User_Score, Computer_Score

    # Get user's choice from HTML
    user_input = request.form["choice"].lower()

    # Computer randomly chooses 1, 2, or 3
    computer_value = np.random.randint(1, 4)

    # Convert number into choice
    if computer_value == 1:
        computer_choice = "rock"

    elif computer_value == 2:
        computer_choice = "paper"

    else:
        computer_choice = "scissors"

    # Game logic
    if user_input == computer_choice:

        result = "It's a TIE!"

    elif (
        (user_input == "rock" and computer_choice == "scissors")
        or
        (user_input == "paper" and computer_choice == "rock")
        or
        (user_input == "scissors" and computer_choice == "paper")
    ):

        result = "YOU WIN!"
        User_Score += 1

    else:

        result = "COMPUTER WINS!"
        Computer_Score += 1

    # Send values to HTML
    return render_template(
        "index.html",
        user_choice=user_input,
        computer_choice=computer_choice,
        result=result,
        User_Score=User_Score,
        Computer_Score=Computer_Score
    )


@app.route("/reset")
def reset():

    global User_Score, Computer_Score

    User_Score = 0
    Computer_Score = 0

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)