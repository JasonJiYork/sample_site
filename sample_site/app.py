from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():

    # Load current count
    f = open("count.txt", "r")
    count = int(f.read())
    f.close()

    # Increment the count
    count += 1

    # Overwrite the count
    f = open("count.txt", "w")
    f.write(str(count))
    f.close()

    # Load current winners
    f = open("winners.txt", "r")
    winners = int(f.read())
    f.close()

    # Increment the winners
    if count % 3 == 0:
        winners += 1

    # Overwrite the winners
    f = open("winners.txt", "w")
    f.write(str(winners))
    f.close()

    # Load current 
    f = open("ifWin.txt", "r")
    ifWin = str(f.read())
    f.close()

    # Increment the 
    if count % 3 == 0:
        ifWin = "Congratulations you have won!"
    else:
        ifWin = "No win"

    # Overwrite the 
    f = open("ifWin.txt", "w")
    f.write(str(ifWin))
    f.close()

        # Load current 
    f = open("winGif.txt", "r")
    winGif = str(f.read())
    f.close()

    # Increment the 
    if count % 3 == 0:
        winGif = "https://c.tenor.com/YWvl8RmENwoAAAAC/baby-kotarou.gif"
    else:
        winGif = ""

    # Overwrite the 
    f = open("winGif.txt", "w")
    f.write(str(winGif))
    f.close()
    
    # Render HTML with count and winner variables
    return render_template("index.html", count=count, winners=winners, ifWin=ifWin, winGif=winGif)



if __name__ == "__main__":
    app.run()

