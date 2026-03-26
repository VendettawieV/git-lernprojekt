# 🌿 Übung 02 – Branches & Commits

## Lernziel
Du lernst, wie man einen eigenen Branch erstellt, darin arbeitet
und ihn wieder in den Hauptbranch überführt (Merge).

## Aufgabe

1. Erstelle einen neuen Branch und wechsle sofort dorthin:
```bash
git checkout -b feature/begruessung
```

2. Öffne die Datei `rechner.py` – du siehst ein `TODO`.
   Ersetze es durch folgende Funktion:

```python
def begruessung(uhrzeit):
    if uhrzeit < 12:
        return "Guten Morgen!"
    elif uhrzeit < 18:
        return "Guten Tag!"
    else:
        return "Guten Abend!"
```

3. Speichere und committe die Änderung:
```bash
git add rechner.py
git commit -m "Begrüßungsfunktion nach Uhrzeit hinzugefügt"
```

4. Wechsle zurück zum Hauptbranch und merge deinen Branch:
```bash
git checkout main
git merge feature/begruessung
```

5. Kontrolliere das Ergebnis:
```bash
git log --oneline --graph
```

## ✅ Erfolgreich, wenn...
- [ ] `git log --graph` den Branch und den Merge anzeigt
- [ ] Die neue Funktion in `rechner.py` auf `main` vorhanden ist
