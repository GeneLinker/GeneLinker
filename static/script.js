// This file is for the client-side JavaScript code

// This function sends a GET request to the server with the query sequence as a querystring parameter
// and the API key as a header
function sendQuerySequence(querySequence) {
  const apiKey = getApiKey(); // get the API key from local storage
  const xhr = new XMLHttpRequest();
  xhr.open("GET", `/federated_hits?query=${querySequence}`);
  xhr.setRequestHeader("Authorization", apiKey);
  xhr.onload = function () {
    if (xhr.status === 200) {
      const response = JSON.parse(xhr.responseText);
      displayHits(response.hits);
    } else if (xhr.status === 403) {
      displayError("Unauthorized access. Please provide a valid API key.");
    } else {
      displayError("An error occurred. Please try again later.");
    }
  };
  xhr.send();
}

// This function gets the API key from local storage
function getApiKey() {
  return localStorage.getItem("apiKey");
}

// This function displays the hits on the webpage
function displayHits(hits) {
  const hitsList = document.getElementById("hits-list");
  hitsList.innerHTML = ""; // clear the previous hits
  for (let i = 0; i < hits.length; i++) {
    const hit = hits[i];
    const hitItem = document.createElement("li");
    hitItem.textContent = `${hit.id}: ${hit.score}`;
    hitsList.appendChild(hitItem);
  }
}

// This function displays an error message on the webpage
function displayError(errorMessage) {
  const errorDiv = document.getElementById("error");
  errorDiv.textContent = errorMessage;
}