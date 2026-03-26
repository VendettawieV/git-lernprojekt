# 🔍 Übung 05 – Git Log & History erkunden

## Lernziel
Du lernst, die Git-Historie zu lesen und gezielt nach Änderungen zu suchen.

## Aufgabe

Führe die folgenden Befehle aus und beantworte die Fragen:

---

### 🔹 Befehl 1: Übersicht aller Commits
```bash
git log --oneline --all --graph
```
**Frage:** Wie viele Branches siehst du? Welcher ist der neueste Commit?

---

### 🔹 Befehl 2: Details zu einem Commit
```bash
git show HEAD
```
**Frage:** Was wurde im letzten Commit geändert?

---

### 🔹 Befehl 3: Wer hat was geändert? (Blame)
```bash
git blame rechner.py
```
**Frage:** Wer hat welche Zeile zuletzt geändert und wann?

---

### 🔹 Befehl 4: Zwei Commits vergleichen
```bash
git diff HEAD~1 HEAD
```
**Frage:** Was hat sich im letzten Commit verändert?

---

### 🔹 Befehl 5: Commit-Nachricht durchsuchen
```bash
git log --all --oneline --grep="Bug"
```
**Frage:** Welche Commits erwähnen den Begriff "Bug"?

---

## ✅ Erfolgreich, wenn...
- [ ] Du alle 5 Fragen beantworten kannst
- [ ] Du weißt, wann du welchen Befehl einsetzt
