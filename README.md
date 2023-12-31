# Developing a Simple Webserver

# AIM:

To develop a simple webserver to serve html programming pages.

## DESIGN STEPS:

### Step 1:

HTML content creation is done

### Step 2:

Design of webserver workflow

### Step 3:

Implementation using Python code

### Step 4:

Serving the HTML pages.

### Step 5:

Testing the webserver

## PROGRAM:
## HTML:
```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dynamic Text Display</title>
  <style>
    body { display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; background-color: #f4f4f4; }
    #container { text-align: center; }
    #square { height: 200px; width: 400px; background: #ffd700; padding: 20px; border-radius: 10px; cursor: pointer; transition: background 0.3s; }
    #square:hover { background: #e0b700; }
    #counter, #resetButton { margin-top: 20px; font-size: 18px; }
    #resetButton { margin-top: 10px; background: #3498db; color: #fff; padding: 10px 20px; border: none; border-radius: 5px; font-size: 16px; cursor: pointer; transition: background 0.3s; }
    #resetButton:hover { background: #2980b9; }
  </style>
  <script>
    document.addEventListener('DOMContentLoaded', function () {
      const phrases = ["Many hands make light work.", "Strike while the iron is hot.", "Honesty is the best policy.", "The grass is always greener on the other side of the fence.", "Don't judge a book by its cover.", "An apple a day keeps the doctor away.", "Better late than never.", "Don't bite the hand that feeds you."];
      let clickCount = 0, square = document.getElementById("square"), counter = document.getElementById("counter");

      function changeText() {
        square.innerHTML = phrases[Math.floor(Math.random() * phrases.length)];
        counter.textContent = `Click Count: ${++clickCount}`;
      }

      function resetCounter() {
        clickCount = 0;
        counter.textContent = `Click Count: ${clickCount}`;
      }

      square.addEventListener('click', changeText);
      document.getElementById("resetButton").addEventListener('click', resetCounter);
    });
  </script>
</head>
<body>
  <div id="container">
    <h2>Dynamic Text Display</h2>
    <div id="square">Click me to change the text.</div>
    <div id="counter">Click Count: 0</div>
    <button id="resetButton">Reset Counter</button>
  </div>
</body>
</html>
```
## PYTHON:
```
import http.server
import socketserver
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'myWebPage.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
# Create an object of the above class
handler_object = MyHttpRequestHandler

# Set the port number for the server
PORT = 8080

# Create the server and bind it to the specified port
my_server = socketserver.TCPServer(("", PORT), handler_object)

print(f"Serving on port {PORT}....")

# Start the server - run indefinately
my_server.serve_forever()
```

## OUTPUT:
## CLIENT SIDE:
![Screenshot 2023-12-31 122051](https://github.com/gowriganeshns/webserver/assets/151705853/2dc0de71-0dab-4989-8c87-aabc798dbca5)
## SERVER SIDE:
![Screenshot 2023-12-31 122143](https://github.com/gowriganeshns/webserver/assets/151705853/651f2f6d-0699-4e1d-b3a0-8f20115775f7)



## RESULT:
The program is executed succesfully
