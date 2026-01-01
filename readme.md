# 🎮 Czerwona Kulka – Gra w Pythonie (Pygame)

Prosta gra inspirowana "biegającym dinozaurem" z Google, ale z **czerwoną kulką** jako głównym bohaterem. Projekt stworzony z myślą o nauce programowania dla dzieci — zawiera prosty i dobrze skomentowany kod w Pythonie.

---

## 📥 Instalacja na Windows

### 1️⃣ Wymagania

* Windows 10 / 11
* Python 3.10 lub nowszy
* Biblioteka **pygame**

Sprawdź, czy Python jest zainstalowany:

```sh
python --version
```

Jeśli nie — pobierz:
[https://www.python.org/downloads/](https://www.python.org/downloads/)

Podczas instalacji pamiętaj zaznaczyć:
☑ Add Python to PATH

---

### 2️⃣ Pobierz projekt

Jeśli używasz Git:

```sh
git clone https://github.com/<TWOJE_REPO>/czerwona-kulka.git
cd czerwona-kulka
```

Lub pobierz i rozpakuj ZIP z repozytorium.

---

### 3️⃣ Utwórz i aktywuj wirtualne środowisko

```sh
python -m venv venv
```

Aktywacja:

```sh
.\\venv\\Scripts\\activate
```

Po aktywacji zobaczysz `(venv)` przed ścieżką — jesteś w środowisku ✔

---

### 4️⃣ Instalacja pygame

```sh
pip install pygame
```

---

## ▶️ Uruchomienie gry

Będąc w folderze gry:

```sh
python runner.py
```

---

## ⌨️ Sterowanie

| Klawisz             | Akcja |
| ------------------- | ----- |
| Spacja / Strzałka ↑ | Skok  |

---

## 📂 Struktura projektu

```
czerwona-kulka/
│
├── runner.py        # główny plik gry
├── skok.wav           # efekt dźwiękowy skoku
├── README.md          # ten plik
└── assets/            # dodatkowe pliki (opcjonalnie)
```

---

## 💡 Pomysły na rozwój

* Animacja oka i min
* System żyć i ekran „Game Over”
* Zbieranie punktów i bonusów
* Menu startowe
* Wybór skórki kulki

---

## 🤝 Współpraca

Pull Requesty mile widziane!
Możesz dodać nowe przeszkody, dźwięki lub grafiki 🎨

---

## 📜 Licencja

Tu możesz dodać wybraną licencję, np. MIT
