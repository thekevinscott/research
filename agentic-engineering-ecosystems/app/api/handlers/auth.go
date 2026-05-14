package handlers

import (
	"crypto/hmac"
	"crypto/sha256"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"os"
	"strings"
	"time"
)

var (
	clientID     = os.Getenv("GITHUB_CLIENT_ID")
	clientSecret = os.Getenv("GITHUB_CLIENT_SECRET")
	sessionKey   = os.Getenv("SESSION_SECRET")
)

func GitHubLogin(w http.ResponseWriter, r *http.Request) {
	redirectURL := fmt.Sprintf(
		"https://github.com/login/oauth/authorize?client_id=%s&scope=repo&redirect_uri=%s",
		clientID,
		url.QueryEscape("http://localhost:8080/auth/callback"),
	)
	http.Redirect(w, r, redirectURL, http.StatusTemporaryRedirect)
}

func GitHubCallback(w http.ResponseWriter, r *http.Request) {
	code := r.URL.Query().Get("code")
	if code == "" {
		http.Error(w, "missing code", http.StatusBadRequest)
		return
	}

	token, err := exchangeCode(code)
	if err != nil {
		http.Error(w, "token exchange failed: "+err.Error(), http.StatusInternalServerError)
		return
	}

	signed := signToken(token)
	http.SetCookie(w, &http.Cookie{
		Name:     "session",
		Value:    signed,
		Path:     "/",
		HttpOnly: true,
		SameSite: http.SameSiteLaxMode,
		MaxAge:   86400 * 7,
	})

	http.Redirect(w, r, "http://localhost:5173", http.StatusTemporaryRedirect)
}

func Me(w http.ResponseWriter, r *http.Request) {
	token, err := getToken(r)
	if err != nil {
		http.Error(w, "unauthorized", http.StatusUnauthorized)
		return
	}

	req, _ := http.NewRequest("GET", "https://api.github.com/user", nil)
	req.Header.Set("Authorization", "Bearer "+token)
	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		http.Error(w, "github api error", http.StatusBadGateway)
		return
	}
	defer resp.Body.Close()

	w.Header().Set("Content-Type", "application/json")
	io.Copy(w, resp.Body)
}

func getToken(r *http.Request) (string, error) {
	cookie, err := r.Cookie("session")
	if err != nil {
		return "", err
	}
	return verifyToken(cookie.Value)
}

func exchangeCode(code string) (string, error) {
	data := url.Values{
		"client_id":     {clientID},
		"client_secret": {clientSecret},
		"code":          {code},
	}

	req, _ := http.NewRequest("POST", "https://github.com/login/oauth/access_token", strings.NewReader(data.Encode()))
	req.Header.Set("Accept", "application/json")
	req.Header.Set("Content-Type", "application/x-www-form-urlencoded")

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	var result struct {
		AccessToken string `json:"access_token"`
		Error       string `json:"error"`
	}
	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		return "", err
	}
	if result.Error != "" {
		return "", fmt.Errorf("oauth error: %s", result.Error)
	}
	return result.AccessToken, nil
}

func signToken(token string) string {
	mac := hmac.New(sha256.New, []byte(sessionKey))
	mac.Write([]byte(token))
	sig := base64.RawURLEncoding.EncodeToString(mac.Sum(nil))
	encoded := base64.RawURLEncoding.EncodeToString([]byte(token))
	return encoded + "." + sig
}

func verifyToken(signed string) (string, error) {
	parts := strings.SplitN(signed, ".", 2)
	if len(parts) != 2 {
		return "", fmt.Errorf("invalid session")
	}
	tokenBytes, err := base64.RawURLEncoding.DecodeString(parts[0])
	if err != nil {
		return "", err
	}
	token := string(tokenBytes)

	mac := hmac.New(sha256.New, []byte(sessionKey))
	mac.Write([]byte(token))
	expected := base64.RawURLEncoding.EncodeToString(mac.Sum(nil))

	if !hmac.Equal([]byte(parts[1]), []byte(expected)) {
		return "", fmt.Errorf("invalid signature")
	}
	return token, nil
}

func init() {
	if sessionKey == "" {
		sessionKey = "dev-secret-change-me"
	}
	_ = time.Now()
}
