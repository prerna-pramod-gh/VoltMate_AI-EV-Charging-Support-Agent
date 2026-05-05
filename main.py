<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Customer Support Agent</title>
    <style>
        /* DESIGN: Modern Terminal / Console Look */
        
        body {
            margin: 0;
            padding: 0;
            background-color: #1e1e1e; /* Dark background like VS Code */
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .terminal-window {
            width: 600px;
            height: 500px;
            background-color: #000000; /* Black console background */
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 20px 50px rgba(0,0,0,0.5);
            display: flex;
            flex-direction: column;
            border: 1px solid #333;
        }

        /* 1. THE HEADER (Matches your Python Output Title) */
        .terminal-header {
            background-color: #1a1a1a;
            padding: 15px;
            border-bottom: 1px solid #333;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .title-text {
            color: #00ff00; /* Terminal Green */
            font-size: 16px;
            font-weight: bold;
            font-family: 'Courier New', Courier, monospace; /* Coding font */
        }

        /* 2. THE CHAT BODY */
        .terminal-body {
            flex: 1;
            padding: 20px;
            overflow-y: auto;
            font-family: 'Courier New', Courier, monospace;
            color: #cccccc;
            font-size: 14px;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        /* Message Styles */
        .message {
            line-height: 1.4;
            padding-bottom: 5px;
        }

        .user-msg {
            color: #ffffff;
        }

        .user-msg::before {
            content: "You: ";
            color: #00ff00; /* Green prompt */
            font-weight: bold;
        }

        .bot-msg {
            color: #e0e0e0;
        }

        .bot-msg::before {
            content: "Bot: ";
            color: #0099ff; /* Blue for bot */
            font-weight: bold;
        }

        /* Escalation Alert Style */
        .escalation-msg {
            color: #ff4444;
            font-weight: bold;
            background: rgba(255, 0, 0, 0.1);
            padding: 5px;
            border-left: 3px solid #ff4444;
        }

        .escalation-msg::before {
            content: "[SYSTEM]: ";
            color: #ff4444;
        }

        /* 3. INPUT AREA */
        .input-area {
            display: flex;
            padding: 15px;
            background-color: #111;
            border-top: 1px solid #333;
        }

        input[type="text"] {
            flex: 1;
            background: transparent;
            border: none;
            color: #00ff00;
            font-family: 'Courier New', Courier, monospace;
            font-size: 16px;
            outline: none;
            caret-color: #00ff00;
        }

        input[type="text"]::placeholder {
            color: #555;
        }

        button {
            background: #333;
            border: 1px solid #00ff00;
            color: #00ff00;
            padding: 5px 15px;
            cursor: pointer;
            font-family: 'Courier New', Courier, monospace;
            font-weight: bold;
            border-radius: 4px;
        }

        button:hover {
            background: #00ff00;
            color: #000;
        }

        /* Scrollbar styling */
        .terminal-body::-webkit-scrollbar {
            width: 8px;
        }
        .terminal-body::-webkit-scrollbar-thumb {
            background: #444;
            border-radius: 4px;
        }

    </style>
</head>
<body>

    <div class="terminal-window">
        <!-- THE HEADER YOU REQUESTED -->
        <div class="terminal-header">
            <div class="title-text">🤖 AI Customer Support Bot (Type 'quit' to exit)</div>
        </div>

        <!-- CHAT AREA -->
        <div class="terminal-body" id="chatBox">
            <div class="message bot-msg">System Online. How can I assist you today?</div>
        </div>

        <!-- INPUT AREA -->
        <div class="input-area">
            <input type="text" id="userInput" placeholder="Type your message here..." onkeypress="handleEnter(event)">
            <button onclick="sendMessage()">Send</button>
        </div>
    </div>

    <script>
        function handleEnter(event) {
            if (event.key === "Enter") {
                sendMessage();
            }
        }

        function sendMessage() {
            var input = document.getElementById("userInput");
            var text = input.value.trim();
            
            if (text === "") return;

            // 1. Display User Message
            addMessage(text, 'user-msg');
            input.value = "";

            // 2. Check for 'quit' command (Matching your Python code)
            if (text.toLowerCase() === 'quit') {
                addMessage("Session ended. Goodbye!", 'bot-msg');
                document.getElementById('userInput').disabled = true; // Disable input
                return;
            }

            // 3. Process Logic
            setTimeout(function() {
                processLogic(text);
            }, 500);
        }

        function addMessage(text, styleClass) {
            var chatBox = document.getElementById("chatBox");
            var msgDiv = document.createElement("div");
            msgDiv.classList.add("message", styleClass);
            msgDiv.innerText = text;
            chatBox.appendChild(msgDiv);
            chatBox.scrollTop = chatBox.scrollHeight;
        }

        // --- THE LOGIC (Matches your Python code) ---
        function processLogic(userText) {
            var lowerText = userText.toLowerCase();
            
            // Frustration Keywords
            var frustrationKeywords = ["angry", "stupid", "hate", "manager", "worst", "bad", "help me"];
            var isFrustrated = frustrationKeywords.some(keyword => lowerText.includes(keyword));

            if (isFrustrated) {
                // Escalation Logic
                addMessage("⚠️ ESCALATION ALERT", 'escalation-msg');
                addMessage("Frustration detected. Creating Ticket #AIS-102...", 'escalation-msg');
                addMessage("Connecting you to a human agent...", 'bot-msg');
            } else {
                // Normal Response
                var responses = [
                    "I can help you with that.",
                    "Processing your request...",
                    "Have you tried restarting the device?",
                    "Our business hours are 9 AM to 5 PM."
                ];
                var randomResponse = responses[Math.floor(Math.random() * responses.length)];
                addMessage(randomResponse, 'bot-msg');
            }
        }
    </script>

</body>
</html>
