# 📝 Übung 01 – Dein erster Commit

## Lernziel
Du lernst, wie man Änderungen mit Git speichert (Commit).

## Aufgabe

1. Erstelle eine neue Datei namens `mein-code.py` im Hauptordner.
2. Schreibe folgenden Inhalt hinein:

```python
def hallo(name):
    print(f"Hallo, {name}!")

hallo("Welt")
```

3. Füge die Datei zum Staging-Bereich hinzu:
```bash
git add mein-code.py
```

4. Erstelle einen Commit mit einer sinnvollen Nachricht:
```bash
git commit -m "Hallo-Welt Funktion hinzugefügt"
```

5. Schau dir danach die Commit-Historie an:
```bash
git log --oneline
```

## ✅ Erfolgreich, wenn...
- [ ] `git log --oneline` deinen neuen Commit anzeigt
- [ ] Die Datei `mein-code.py` existiert und ausführbar ist

public class TestScript : Monobehavior {
    void Update(){
        transform.Translate(Vector3.forward * Time.deltaTime);
    }
}