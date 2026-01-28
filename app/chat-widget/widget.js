console.log("✅ widget.js loaded");

// 🔹 CONFIG — must be at TOP
const BUSINESS_ID = "demo-business";
const API_URL = "http://localhost:8000/chat";

// 🔹 DOM elements
const sendBtn = document.getElementById("sendBtn");
const input = document.getElementById("messageInput");
const messagesDiv = document.getElementById("chat-messages");

// 🔹 Event binding
sendBtn.addEventListener("click", sendMessage);

// 🔹 Helper to show messages
function addMessage(text, sender) {
  const msgDiv = document.createElement("div");
  msgDiv.innerText = (sender === "user" ? "You: " : "Bot: ") + text;
  messagesDiv.appendChild(msgDiv);
}

// 🔹 Send message to backend
async function sendMessage() {
  console.log("👉 Send button clicked");

  const message = input.value;
  if (!message) return;

  addMessage(message, "user");
  input.value = "";

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        business_id: BUSINESS_ID,
        question: message
      })
    });

    const data = await response.json();
    console.log("✅ API response:", data);

    addMessage(data.answer || "No reply", "bot");

  } catch (error) {
    console.error("❌ Fetch failed:", error);
    addMessage("Error connecting to server", "bot");
  }
}
