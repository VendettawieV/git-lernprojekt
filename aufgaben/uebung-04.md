# ↩️ Übung 04 – Fehler rückgängig machen

## Lernziel
Du lernst, wie man einen fehlerhaften Commit sicher rückgängig macht,
ohne die Git-Historie zu löschen (`git revert`).

## Hintergrund
Jemand hat einen Bug in `rechner.py` eingecheckt:
Die `dividiere()`-Funktion gibt immer `0` zurück – das muss weg!

## Aufgabe

1. Schau dir die Commit-Historie an:
```bash
git log --oneline
```

2. Du siehst einen Commit mit der Nachricht:
   `"Division implementiert (mit Bug)"`
   Notiere dir die Commit-ID (z.B. `a3f9c12`).

3. Mache diesen Commit rückgängig:
```bash
git revert <COMMIT-ID>
```

4. Git öffnet einen Editor für die Commit-Nachricht.
   Einfach speichern und schließen (`:wq` in vim, oder Fenster schließen in VS Code).

5. Prüfe, ob der Bug behoben ist:
```bash
python3 rechner.py
```

## ⚠️ revert vs. reset – Was ist der Unterschied?

| Befehl       | Was passiert?                                      | Sicher im Team? |
|--------------|----------------------------------------------------|-----------------|
| `git revert` | Erstellt einen **neuen** Commit, der rückgängig macht | ✅ Ja          |
| `git reset`  | **Löscht** Commits aus der Historie               | ⛔ Gefährlich   |

Im Team-Umfeld benutzt man fast immer `git revert`!

## ✅ Erfolgreich, wenn...
- [ ] `git log --oneline` einen neuen "Revert"-Commit zeigt
- [ ] Die Division in `rechner.py` wieder korrekt funktioniert
