# ⚡ Übung 03 – Merge Conflict lösen

## Lernziel
Du verstehst, warum Merge Conflicts entstehen und wie man sie löst.

## Hintergrund
Zwei Entwickler haben gleichzeitig dieselbe Zeile in `rechner.py` geändert.
Wenn du die Branches zusammenführst, entsteht ein Konflikt.

## Aufgabe

1. Schau dir zuerst die beiden Branches an:
```bash
git log --oneline --all --graph
```

2. Merge `conflict-a` in den aktuellen Branch:
```bash
git merge conflict-a
```

3. Git meldet einen Konflikt! Öffne `rechner.py`.
   Du siehst Markierungen wie:
```
<<<<<<< HEAD
    return a + b  # Version B (direkt)
=======
    result = a + b  # Version A (mit Zwischenvariable)
    return result
>>>>>>> conflict-a
```

4. Entscheide, welche Version richtig ist (oder kombiniere beide).
   Entferne anschließend alle `<<<<<<<`, `=======`, `>>>>>>>` Zeilen.

5. Schließe den Merge ab:
```bash
git add rechner.py
git commit -m "Merge Conflict in rechner.py aufgelöst"
```

## 💡 Tipp
VS Code zeigt Konflikte sehr übersichtlich an mit Buttons:
"Accept Current Change" / "Accept Incoming Change" / "Accept Both Changes"

## ✅ Erfolgreich, wenn...
- [ ] `git status` keine Konflikte mehr meldet
- [ ] `rechner.py` keine `<<<<<<<` Markierungen mehr enthält
- [ ] Der Merge-Commit in `git log` sichtbar ist
