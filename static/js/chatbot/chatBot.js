const chatbox = document.getElementById("chatbox");
const chatContainer = document.getElementById("chat-container");
const userInput = document.getElementById("user-input");
const sendButton = document.getElementById("send-button");
const openChatButton = document.getElementById("open-chat");
const closeChatButton = document.getElementById("close-chat");

let isChatboxOpen = true; // Set the initial state to open

// Function to toggle the chatbox visibility
function toggleChatbox() {
	chatContainer.classList.toggle("hidden");
	isChatboxOpen = !isChatboxOpen; // Toggle the state
}

// Add an event listener to the open chat button
openChatButton.addEventListener("click", toggleChatbox);

// Add an event listener to the close chat button
closeChatButton.addEventListener("click", toggleChatbox);

// Add an event listener to the send button
sendButton.addEventListener("click", function () {
	const userMessage = userInput.value;
	if (userMessage.trim() !== "") {
		addUserMessage(userMessage);
		sendChatMessages(); // Send chat messages to Django backend
		userInput.value = "";
	}
});

userInput.addEventListener("keyup", function (event) {
	const userMessage = userInput.value;
	if (event.key === "Enter") {

		if (userMessage.trim() !== "") {
			addUserMessage(userMessage);
			userInput.value = "";
			sendChatMessages(); // Send chat messages to Django backend
		}
	}
});

function addUserMessage(message) {
	const messageElement = document.createElement("div");
	messageElement.classList.add("mb-2", "text-right");
	messageElement.innerHTML = `<p class="bg-cyan-800 text-white rounded-lg py-2 px-4 inline-block">${message}</p>`;
	chatbox.appendChild(messageElement);
	chatbox.scrollTop = chatbox.scrollHeight;
}

function addBotMessage(message) {
	const messageElement = document.createElement("div");
	messageElement.classList.add("mb-2");
	messageElement.innerHTML = `<p class="bg-gray-200 text-gray-700 rounded-lg py-2 px-4 inline-block">${message}</p>`;
	chatbox.appendChild(messageElement);
	chatbox.scrollTop = chatbox.scrollHeight;
}

// Function to send chat messages to Django backend
function sendChatMessages() {
	const messages = [];
	// Collect all chat messages
	document.querySelectorAll("#chatbox .bg-blue-500, #chatbox .bg-gray-200").forEach((messageElement) => {
		const messageText = messageElement.textContent.trim();
		const messageType = messageElement.classList.contains("bg-blue-500") ? "user" : "assistant";
		messages.push({ message: messageText, type: messageType });
	});

	// Send messages to Django backend via AJAX
	fetch("/message-to-bot/", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
			"X-CSRFToken": getCookie("csrftoken"), // Include CSRF token
		},
		body: JSON.stringify({ messages: messages }),
	})
		.then(response => {
			if (!response.ok) {
				throw new Error("Network response was not ok");
			}
			return response.json(); // Parse JSON response
		})
		.then(data => {
			const botResponseText = data.bot_response; // Extract bot response text
			addBotMessage(botResponseText); // Add bot response to chat
		})
		.catch(error => {
			console.error("There was a problem with the chat message request:", error);
		});
}

function respondToUser(userMessage) {
	// Replace this with your chatbot logic
	setTimeout(() => {
		addBotMessage(userMessage);
	}, 500);
}

// Function to get CSRF token
function getCookie(name) {
	let cookieValue = null;
	if (document.cookie && document.cookie !== "") {
		const cookies = document.cookie.split(";");
		for (let i = 0; i < cookies.length; i++) {
			const cookie = cookies[i].trim();
			if (cookie.substring(0, name.length + 1) === (name + "=")) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}