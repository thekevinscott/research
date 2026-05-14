package handlers

import (
	"encoding/json"
	"io"
	"net/http"
)

func ListRepos(w http.ResponseWriter, r *http.Request) {
	token, err := getToken(r)
	if err != nil {
		http.Error(w, "unauthorized", http.StatusUnauthorized)
		return
	}

	req, _ := http.NewRequest("GET", "https://api.github.com/user/repos?sort=updated&per_page=50", nil)
	req.Header.Set("Authorization", "Bearer "+token)
	req.Header.Set("Accept", "application/vnd.github.v3+json")

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		http.Error(w, "github api error", http.StatusBadGateway)
		return
	}
	defer resp.Body.Close()

	if resp.StatusCode != 200 {
		body, _ := io.ReadAll(resp.Body)
		http.Error(w, string(body), resp.StatusCode)
		return
	}

	var repos []struct {
		FullName    string `json:"full_name"`
		Description string `json:"description"`
		Language    string `json:"language"`
		UpdatedAt   string `json:"updated_at"`
		Private     bool   `json:"private"`
		HTMLURL     string `json:"html_url"`
	}

	if err := json.NewDecoder(resp.Body).Decode(&repos); err != nil {
		http.Error(w, "decode error", http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(repos)
}
