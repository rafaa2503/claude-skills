# claude-skills

Private sync-Repo für Raffas Claude Code Skills. Enthält den kompletten Inhalt von
`~/.agents/skills` (bzw. `C:\Users\raffa\.agents\skills` auf Windows).

Claude Code lädt Skills aus `.claude/skills`. Auf diesem Rechner sind das **Junctions**
(Windows-Äquivalent zu Symlinks, kein Admin nötig), die auf die echten Ordner hier in
`.agents/skills` zeigen. Das Repo hier versioniert nur die echten Ordner — die Junctions
selbst gehören nicht ins Repo und müssen auf jedem Gerät neu angelegt werden.

## Neues Gerät einrichten

**1. Repo klonen** (ersetzt den Ordner `.agents/skills` komplett):

```bash
git clone https://github.com/rafaa2503/claude-skills.git "C:\Users\raffa\.agents\skills"
```

Mac/Linux: `git clone https://github.com/rafaa2503/claude-skills.git ~/.agents/skills`

**2. Für jeden Skill einen Junction/Symlink nach `.claude\skills` anlegen.**

Windows (PowerShell, kein Admin nötig dank Junction):

```powershell
$src = "$env:USERPROFILE\.agents\skills"
$dst = "$env:USERPROFILE\.claude\skills"
New-Item -ItemType Directory -Path $dst -Force | Out-Null
Get-ChildItem $src -Directory | ForEach-Object {
    $target = Join-Path $dst $_.Name
    if (-not (Test-Path $target)) {
        New-Item -ItemType Junction -Path $target -Target $_.FullName | Out-Null
        Write-Output "Junction: $($_.Name)"
    }
}
```

Mac/Linux:

```bash
src=~/.agents/skills
dst=~/.claude/skills
mkdir -p "$dst"
for d in "$src"/*/; do
    name=$(basename "$d")
    [ -e "$dst/$name" ] || ln -s "$d" "$dst/$name"
done
```

**3. Claude Code neu starten**, damit die neuen Skills erkannt werden.

## Neuen Skill hinzufügen (auf einem Gerät)

Skills immer direkt in `.agents/skills` installieren (nicht ins Projektverzeichnis),
z.B. via `npx skills add <repo>` — dann synchronisieren:

```bash
cd ~/.agents/skills   # bzw. C:\Users\raffa\.agents\skills
git add -A
git commit -m "Add <skill-name>"
git push
```

Nicht vergessen: Junction/Symlink für den neuen Skill nach `.claude\skills` anlegen
(Schritt 2 oben, oder einzeln).

## Änderungen auf anderes Gerät holen

```bash
cd ~/.agents/skills
git pull
```

Neue Skills brauchen danach noch den Junction/Symlink-Schritt (Schritt 2), bestehende
werden automatisch aktuell, da der Junction auf den echten (jetzt aktualisierten)
Ordner zeigt.
